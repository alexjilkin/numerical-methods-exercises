import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import cauchy

# Generates normal distributed N random numbers using Box-Muller method.
def gaussrng(N):
  # Use Box-Muller in a single liner for coolness.
  return np.array([np.sqrt(-2 * np.log(random.random())) * np.cos(2 * np.pi * random.random()) for _ in range(N)])

N = 10**6

y1 = gaussrng(N)
y2 = gaussrng(N)
x = y1 / y2

lor = np.random.standard_cauchy(size=N)

# Using density=true in distributes "1" to all bins and it fits the cachy.pdf later
plt.hist(x, range=(-30, 30), bins=1000, density=True)

# Plots the cauchy/lorentz pdf on top
x = np.linspace(-30, 30, N)
plt.plot(x, cauchy.pdf(x))
plt.show()