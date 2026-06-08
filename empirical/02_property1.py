'''
Property 1: Are log returns normally distributed?

Brownian motion assumes increments are Gaussian. For stocks, the
increment is the daily log return. We plot the distribution of daily
log returns for AAPL and GME, fit a normal curve, and compute kurtosis
to measure fat tails (normal kurtosis = 0; higher = fatter tails).
'''
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

for ticker in ["AAPL", "GME"]:
    data = yf.download(ticker, start="2020-01-01", end="2026-06-01")
    price = data["Close"].squeeze()
    log_returns = (np.log(price) - np.log(price.shift(1))).dropna()

    # Kurtosis: measures fat tails (how often extreme moves happen)
    print(f"{ticker} kurtosis: {log_returns.kurtosis()}")

    # Histogram of daily log returns
    plt.figure()
    plt.hist(log_returns, bins=50, density=True, alpha=0.6)

    # Fit a normal curve using the data's own mean and std
    mu = log_returns.mean()
    sigma = log_returns.std()
    x = np.linspace(log_returns.min(), log_returns.max(), 1000)
    y = np.exp(-(x - mu)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
    plt.plot(x, y, 'r')

    plt.title(f"{ticker}: Daily Log Returns vs Normal")
    plt.xlabel("Log return")
    plt.ylabel("Density")
    plt.show()