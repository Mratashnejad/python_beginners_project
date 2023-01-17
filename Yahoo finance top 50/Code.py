
#try to get to 50 holdings and symbols from Yahoo Finance and print them out with python.

import yfinance as yf
import pandas as pd

# QQQ ETF symbol
etf_symbol = "QQQ"

# Retrieve the top 50 holdings of the ETF
qqq = yf.Ticker(etf_symbol)
top_50_holdings = qqq.info.get("holdings")[:50]
top_50_symbols = [holding.get("symbol") for holding in top_50_holdings]

print("TOP 50 HOLDING :" ,top_50_holdings)
print("TOP 50 SymBols :", top_50_symbols)

