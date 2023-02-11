import numpy as np
import matplotlib.pyplot as plt
import time 

log = np.log

def f(mu, x):
  return np.exp( log(x) - (log(mu * (x - 1) + 1)) / (mu - 1))

def plot(f):
  x = np.linspace(0.3, 1, 10000)
  plt.plot(x, f(2.5, x), "r-")
  plt.plot(x, f(3, x), "g-")
  plt.plot(x, f(3.2, x), "b-")
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.grid()
  plt.show()

plot(f)