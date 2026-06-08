'''
Property 3: Does variance grow linearly with time?

Brownian motion predicts Var(n-day return) = n x Var(1-day return),
i.e. variance grows linearly with the time horizon. We compute the
variance of n-day log returns for n = 1 to 20 and plot it against n.
A straight line supports Property 3; a bent curve signals deviation
(e.g. mean reversion or time-varying volatility).
'''
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

for ticker in ["AAPL", "GME"]:
    data = yf.download(ticker, start="2020-01-01", end="2026-06-01")
    price = data["Close"].squeeze()

    days = range(1, 21)
    variances = []
    for n in days:
        log_n = np.log(price) - np.log(price.shift(n))   # n-day return
        variances.append(log_n.var())

    plt.figure()
    plt.scatter(days, variances)
    plt.title(f"{ticker}: Variance of Log Returns vs Time")
    plt.xlabel("n (days)")
    plt.ylabel("Variance of log returns")
    plt.show()