<div align="center">
    <h1>Real-time stream processing in Python</h1>
    <i>Compute real-time OHLC data from raw trades with <a href="https://bytewax.io/">Bytewax</a></i>
</div>

<br />

<div align="center">
    <sub>Let's connect 🤗</sub>
    <br />
    <a href="https://github.com/davemachado/public-api">Twitter</a> •
    <a href="https://github.com/public-apis/public-apis/issues">LinkedIn</a> •
    <a href="https://github.com/public-apis/public-apis/pulls">Newsletter</a> 
<br />
</div>


## What is this repo about?
This repository shows how to

* fetch real-time data from an external websocket (in this case, Coinbase Websocket API) 
* process it in real-time using [Bytewax](https://bytewax.io/), and
* plot the processed data (in this case OHLC points) with Streamlit.

The final app is public 👉🏽 [Streamlit app]()

## Quick setup

1. Install [Python Poetry](https://python-poetry.org/)
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. cd into the project folder and run `poetry install`

3. activate the virtual env that you just created with `poetry shell`

To run the Streamlit app locally simply do `streamlit run src/frontend.py`

`