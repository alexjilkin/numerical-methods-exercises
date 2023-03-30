import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, cauchy
import random

Ks = [3, 10, 30, 100]

# Plots an histogram of z values
# rand: a function returning random number
def plot_z(rand):
  for K in Ks:
    # Generate 10^4 mean values of K random numbers
    z_array = [np.mean([rand() for _ in range(K)]) for _ in range(10**4)]
    plt.hist(z_array, bins=100, density=True, label="K={}".format(K))

# Plots the norm pdf in the range [min, max]
def plot_norm(mu, var_base, min, max):
  for K in Ks:
    # I try to generically fit a norm based on the K size
    variance = var_base / K
    sigma = np.sqrt(variance)
    x = np.linspace(min, max, 100)
    plt.plot(x, norm.pdf(x, mu, sigma), label="var={:.4f}".format(variance))


# Uniform distribution
plot_z(lambda: np.random.uniform(-0.5, 0.5))
plot_norm(0, 0.1, -0.5, 0.5)
plt.legend()
plt.show()

# Exp distribution
plot_z(lambda: np.random.exponential())
plot_norm(1, 1, 0, 3)
plt.legend()
plt.show()

# Exp distribution
plot_z(lambda: np.random.standard_cauchy())
plot_norm(1, 1, 0, 3)
plt.legend()
plt.show()