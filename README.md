<div align="center">
    <h1>Real-time stream processing in Python</h1>
    <i>Compute real-time OHLC data from raw trades with <a href="https://bytewax.io/">Bytewax </a></i>
</div>

<br />

<div align="center">
    <sub>Let's connect 🤗</sub>
    <br />
    <a href="https://twitter.com/paulabartabajo_">Twitter</a> •
    <a href="https://www.linkedin.com/in/pau-labarta-bajo-4432074b/">LinkedIn</a> •
    <a href="https://paulabartabajo.substack.com/">Newsletter</a>
<br />
</div>


## What is this repo about?
This repository shows how to

* fetch real-time trade data from the [Coinbase Websocket API](https://help.coinbase.com/en/cloud/websocket-feeds/exchange)
* transform trade data into OHLC data in real-time using [Bytewax](https://bytewax.io/), and
* plot the OHLC data using [Bokeh](https://bokeh.org/) and [Streamlit](https://github.com/streamlit/streamlit).

The final app is publicly deployed on Streamlit Cloud 👉🏽 [click here]()

## Quick setup

1. Install [Python Poetry](https://python-poetry.org/)
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. cd into the project folder and run `poetry install`

3. activate the virtual env that you just created with `poetry shell`

To run the Streamlit app locally simply do `streamlit run src/frontend.py`