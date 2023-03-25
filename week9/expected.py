import numpy as np
import matplotlib.pyplot as plt
import random 

N = 1000
trials = [np.average(np.random.uniform(0, 1, size=1000)) for _ in range(100)]

plt.scatter(np.arange(0, 100), trials)
plt.show()