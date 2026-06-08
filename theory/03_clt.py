'''
Central Limit Theorem

Runs 10,000 random walks of 100 steps each, collects the final
position (sum) of each, and plots their distribution. The result
converges to a normal distribution - this is the CLT, and the
reason Brownian motion's increments are Gaussian.
'''
import numpy as np
import matplotlib.pyplot as plt

# 10,000 experiments, each a random walk of 100 steps
steps = np.random.choice([-1, 1], size=(10000, 100))

# Sum each row -> 10,000 final positions
endpoints = steps.sum(axis=1)

# Histogram of the final positions -> bell shape (normal)
plt.hist(endpoints, bins=50)
plt.title("CLT: Distribution of Random Walk Endpoints")
plt.xlabel("Final position")
plt.ylabel("Frequency")
plt.show()