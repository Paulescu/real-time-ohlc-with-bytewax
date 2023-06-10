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

<p align="center">
  <img src="https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26413f2b-6196-4b16-bc60-bf4e0637a831_931x667.png" width='500' />
</p>

#### Table of contents
1. [What is this repo about?](#what-is-this-repo-about)
2. [How to run this code](#how-to-run-this-code)
3. [Wannna build real-world ML products?](#wannna-build-real-world-ml-products)

## What is this repo about?
This repository shows how to

* fetch real-time trade data from the [Coinbase Websocket API](https://help.coinbase.com/en/cloud/websocket-feeds/exchange)
* transform trade data into OHLC data in real-time using [Bytewax](https://bytewax.io/), and
* plot the OHLC data using [Bokeh](https://bokeh.org/) and [Streamlit](https://github.com/streamlit/streamlit).

The final app is publicly deployed on Streamlit Cloud 👉🏽 [click here](https://paulescu-real-time-ohlc-with-bytewax.streamlit.app/)

## How to run this code

1. Create a Python virtual environment with the project dependencies with
    ```
    $ make init
    ```

2. To run the Streamlit app locally simply do
    ```
    $ make run
    ```

## Wanna learn to design, develop and deploy a real-world ML system yourself?
Join the [Real-World ML Tutorial + Community](https://realworldmachinelearning.carrd.co/) and get LIFETIME ACCESS to

* 3 hours of video lectures 🎬
* Full source code implementation 👨‍💻
* Discord private community, to connect with 100+ students and me 👨‍👩‍👦


