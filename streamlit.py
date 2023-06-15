import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple stock price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'

tickerDate = yf.Ticker(tickerSymbol)

tickerDf = tickerDate.history(period='ld',start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)