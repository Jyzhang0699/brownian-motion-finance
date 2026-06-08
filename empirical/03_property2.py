'''
Property 2: Are returns independent over time?

Brownian motion assumes increments are independent ("no memory").
We test two aspects:
1. Direction: correlation between today's and yesterday's return
   (scatter plot + correlation). Near 0 means no linear dependence.
2. Magnitude: correlation between absolute returns. A positive value
   reveals volatility clustering (big moves follow big moves) - a
   dependence that the simple correlation misses.
'''
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

for ticker in ["AAPL", "GME"]:
    data = yf.download(ticker, start="2020-01-01", end="2026-06-01")
    price = data["Close"].squeeze()
    log_returns = (np.log(price) - np.log(price.shift(1))).dropna()

    # Direction: today vs yesterday
    direction_corr = log_returns.corr(log_returns.shift(1))
    print(f"{ticker} direction correlation: {direction_corr}")

    # Magnitude: absolute returns (volatility clustering)
    abs_returns = log_returns.abs()
    magnitude_corr = abs_returns.corr(abs_returns.shift(1))
    print(f"{ticker} magnitude correlation: {magnitude_corr}")

    # Scatter: today vs yesterday
    plt.figure()
    plt.scatter(log_returns, log_returns.shift(1), s=5)
    plt.title(f"{ticker}: Today vs Yesterday Return")
    plt.xlabel("Today's return")
    plt.ylabel("Yesterday's return")
    plt.show()