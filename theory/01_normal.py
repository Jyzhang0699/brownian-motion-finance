'''
Standard Normal Distribution

Plots the probability density of N(0,1),
the starting point for building Brownian motion.

'''
import numpy as np
import matplotlib.pyplot as plt

# x-axis: 1000 evenly spaced points from -4 to 4
x = np.linspace(-4, 4, 1000)

# y-axis: standard normal probability density function
y = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

plt.plot(x, y)
plt.title("Standard Normal Distribution")
plt.xlabel("x")
plt.ylabel("Probability density")
plt.show()