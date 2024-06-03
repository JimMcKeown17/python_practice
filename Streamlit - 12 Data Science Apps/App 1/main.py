import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
### Simple Stock Price App

Shown are the stock closing price and volume of Apple!
""")

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)

# Adjusted the end date format
tickerDf = tickerData.history(period='1d', start='2014-05-31', end='2024-05-31')
# print(tickerDf)
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("Volume")
st.line_chart(tickerDf.Volume)
