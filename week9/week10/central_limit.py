import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import random

Ks = [3, 10, 30, 100]

# Plots an histogram of z values
# rand: a function returning random number
def plot_z(rand):
  for K in Ks:
      # Generate 10^4 mean values of K random numbers
      z_array = [np.mean([rand() for _ in range(K)]) for _ in range(10**4)]
      plt.hist(z_array, bins=100, density=True, label="K={}".format(K))

      mu = 0
      variance = 0.1 / K
      sigma = np.sqrt(variance)
      x = np.linspace(-0.5, 0.5, 100)
      plt.plot(x, norm.pdf(x, mu, sigma), label="var={:.4f}".format(variance))

  plt.legend()
  plt.show()

plot_z(lambda: random.uniform(-0.5, 0.5))

    