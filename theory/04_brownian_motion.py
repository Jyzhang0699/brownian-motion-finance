'''
Brownian Motion

Constructs Brownian motion as the continuous limit of a random walk:
the time interval [0, T] is split into n steps, each of size sqrt(dt).
The sqrt(dt) scaling keeps the variance finite as n grows, so the
path stays bounded while becoming continuous. Variance grows
linearly with time (Var = T), so larger T spreads the path wider.
'''
import numpy as np
import matplotlib.pyplot as plt

T = 1                          # total time
n = 1000                       # number of steps (the finer, the more continuous)
dt = T / n                     # time per step

t = np.linspace(0, T, n)                              # time axis: 0 to T
steps = np.random.choice([-1, 1], size=n) * np.sqrt(dt)  # each step scaled by sqrt(dt)
position = np.cumsum(steps)                           # accumulate into a path

plt.plot(t, position)
plt.title("Brownian Motion")
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()