import numpy as np
import matplotlib.pyplot as plt

# Generates uniforms random numbers and calculate it's arithmetic mean.
trials_1 = [np.mean(np.random.uniform(0, 1, size=1000)**2) for _ in range(100)]
trials_2 = [np.mean(np.random.uniform(0, 1, size=10**5)**2) for _ in range(100)]

# Plot both
plt.scatter(np.arange(0, 100), trials_1, label="N=1000")
plt.scatter(np.arange(0, 100), trials_2, label="N=10^5")

plt.legend()
plt.show()