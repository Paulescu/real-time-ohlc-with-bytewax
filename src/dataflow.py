import json
from typing import Tuple, Dict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import numpy as np
from websocket import create_connection  # pip install websocket-client
from bytewax.dataflow import Dataflow
from bytewax.execution import spawn_cluster, run_main
from bytewax.inputs import ManualInputConfig
from bytewax.outputs import StdOutputConfig
from bytewax.window import EventClockConfig, TumblingWindowConfig

from src.date_utils import str2epoch, epoch2datetime

@dataclass
class Ticker:
    product_id : str
    ts_unix : int
    price : float
    size : float

PRODUCT_IDS = [
    # "BTC-USD",
    "ETH-USD",
    # "SOL-USD"
]

def ws_input(product_ids, state):
    ws = create_connection("wss://ws-feed.pro.coinbase.com")
    ws.send(
        json.dumps(
            {
                "type": "subscribe",
                "product_ids": product_ids,
                "channels": ["ticker"],
            }
        )
    )
    # The first msg is just a confirmation that we have subscribed.
    print(ws.recv())
    while True:
        yield state, ws.recv()


def input_builder(worker_index, worker_count, resume_state):
    state = resume_state or None
    prods_per_worker = int(len(PRODUCT_IDS) / worker_count)
    product_ids = PRODUCT_IDS[
        int(worker_index * prods_per_worker) : int(
            worker_index * prods_per_worker + prods_per_worker
        )
    ]
    return ws_input(product_ids, state)


def key_on_product(data: Dict) -> Tuple[str, Ticker]:
    """Transform input `data` into a Tuple[product_id, ticker_data]
    where `ticker_data` is a `Ticker` object.

    Args:
        data (Dict): _description_

    Returns:
        Tuple[str, Ticker]: _description_
    """
    ticker = Ticker(
        product_id=data['product_id'],
        ts_unix=str2epoch(data['time']),
        price=data['price'],
        size=data['last_size']
    )
    return (data["product_id"], ticker)

def get_dataflow(
    window_seconds: int
) -> Dataflow:
    """Constructs and returns a ByteWax Dataflow

    Args:
        window_seconds (int)

    Returns:
        Dataflow:
    """
    flow = Dataflow()
    flow.input("input", ManualInputConfig(input_builder))

    # parse string to dictionary
    flow.map(json.loads)

    # (ticker_data) -> (product_id, ticker_obj)
    flow.map(key_on_product)

    def get_event_time(ticker: Ticker) -> datetime:
        """
        This function instructs the event clock on how to retrieve the
        event's datetime from the input.
        """
        return epoch2datetime(ticker.ts_unix)

    def build_array() -> np.array:
        """_summary_

        Returns:
            np.array: _description_
        """
        return np.empty((0,3))

    def acc_values(previous_data: np.array, ticker: Ticker) -> np.array:
        """
        This is the accumulator function, and outputs a numpy array of time and price
        """
        return np.insert(previous_data, 0,
                        np.array((ticker.ts_unix, ticker.price, ticker.size)), 0)

    # Configure the `fold_window` operator to use the event time
    cc = EventClockConfig(get_event_time, wait_for_system_duration=timedelta(seconds=10))

    start_at = datetime.now(timezone.utc)
    start_at = start_at - timedelta(
        seconds=start_at.second, microseconds=start_at.microsecond
    )
    wc = TumblingWindowConfig(start_at=start_at,length=timedelta(seconds=window_seconds))

    flow.fold_window(f"{window_seconds}_sec", cc, wc, build_array, acc_values)


    # compute OHLC for the window
    def calculate_features(ticker_data: Tuple[str, np.array]) -> Tuple[str, Dict]:
        """Aggregate trade data in window

        Args:
            ticker__data (Tuple[str, np.array]): product_id, data

        Returns:
            Tuple[str, Dict]: product_id, Dict with keys
                - time
                - open
                - high
                - low
                - close
                - volume
        """
        ticker, data = ticker_data
        ohlc = {
            "time": data[-1][0],
            "open": data[:,1][-1],
            "high": np.amax(data[:,1]),
            "low":np.amin(data[:,1]),
            "close":data[:,1][0],  
            "volume": np.sum(data[:,2])
        }
        return (ticker, ohlc)

    flow.map(calculate_features)

    # # compute technical-indicators
    # from src.technical_indicators import BollingerBands
    # flow.stateful_map(
    #     "technical_indicators",
    #     lambda: BollingerBands(3),
    #     BollingerBands.compute
    # )

    return flow

if __name__ == "__main__":
    
    # Test inputs/outputs for debuggin
    WINDOW_SECONDS = 5
    flow = get_dataflow(window_seconds=WINDOW_SECONDS)
    flow.capture(StdOutputConfig())
    run_main(flow)