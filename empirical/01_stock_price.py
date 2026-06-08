'''
Stock Prices: AAPL and GME

Downloads daily closing prices for Apple (stable large-cap) and
GameStop (volatile meme stock) from 2020 to 2026. These two contrasting
stocks are used throughout to test how well Brownian motion describes
real markets.
'''
import yfinance as yf
import matplotlib.pyplot as plt

for ticker in ["AAPL", "GME"]:
    data = yf.download(ticker, start="2020-01-01", end="2026-06-01")
    price = data["Close"].squeeze()

    plt.figure()                       # new figure for each stock
    plt.plot(price)
    plt.title(f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()