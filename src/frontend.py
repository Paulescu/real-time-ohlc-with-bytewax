
import pandas as pd
import streamlit as st

from bytewax.outputs import ManualOutputConfig
from bytewax.execution import run_main

from src.plot import get_candlestick_plot
from src.date_utils import epoch2datetime

WINDOW_SECONDS = 30

st.set_page_config(layout="wide")
st.title(f"ETH/USD OHLC data every {WINDOW_SECONDS} seconds")
# st.header('Lines represent Bollinger Bands')

# here we store the data our Stream processing outputs
df = pd.DataFrame()

def output_builder(worker_index, worker_count):
    
    placeholder = st.empty()

    def write_to_dashboard(key__data):
        
        _, data = key__data
        
        # add 'date' key with datetime
        data['date'] = epoch2datetime(data['time'])

        # append one row with the latest observation `data`
        global df
        df = df.append(data, ignore_index=True)

        with placeholder.container():
            p = get_candlestick_plot(df, WINDOW_SECONDS)
            st.bokeh_chart(p, use_container_width=True)

    return write_to_dashboard


from src.dataflow import get_dataflow
flow = get_dataflow(window_seconds=WINDOW_SECONDS)
flow.capture(ManualOutputConfig(output_builder))
run_main(flow)
