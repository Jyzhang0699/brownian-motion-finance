'''
Random Walk

Simulates a discrete random walk: each step is +1 or -1 with equal
probability, accumulated over time. This is the discrete building
block that converges to Brownian motion.
'''
import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random steps, each +1 or -1
steps = np.random.choice([-1, 1], size=1000)

# Cumulative sum: the position after each step (the path)
position = np.cumsum(steps)

plt.plot(position)
plt.title("Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()