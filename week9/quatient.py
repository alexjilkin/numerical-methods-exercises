import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import cauchy

def gaussrng(N):
  # Use Box-Muller in a single liner for coolness.
  return np.array([np.sqrt(-2 * np.log(random.random())) * np.cos(2 * np.pi * random.random()) for _ in range(N)])

N = 10**6

y1 = gaussrng(N)
y2 = gaussrng(N)
x = y1 / y2

lor = np.random.standard_cauchy(size=N)

plt.hist(x, range=(-10, 10), bins=1000, density=True)

x = np.linspace(-10, 10, N)
plt.plot(x, cauchy.pdf(x))
plt.show()