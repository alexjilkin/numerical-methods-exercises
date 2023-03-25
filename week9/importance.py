import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm

k = 1
def f_exp(x):
   return 1.2 * np.exp(-0.5 * x)

def f_exp_cdf(y):
   return 1 - (y/1.2)

def f(x):
    return np.exp(-(x**2)/2)
def f_inv(x):
    return np.sqrt(-2 * np.log(2*x))


def plot_gaus_dist():
   nums = [f_inv(random.uniform(0, 1)) for _ in range(10**5)]
   plt.hist(nums, bins=1000, density=True)
   plt.plot()
   plt.show()
   
def compare():
  x = np.linspace(-5, 5, 1000)
  plt.plot(x, f_exp(x), label="exp")
  plt.plot(x, f(x), label="guassian")
  plt.legend()
  plt.show()

# compare()
# plot_gaus_dist()

x = np.linspace(-10, 10, 1000)
plt.plot(x, f_exp_cdf(x))
plt.show()