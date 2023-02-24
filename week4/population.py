import numpy as np
import matplotlib.pyplot as plt

# Calculated f including complex values
def f(mu, x):
  return np.power((mu * (x - 1) + 1) / x, 1 / (mu - 1), dtype=complex)

# Plots the real part of f, with different arguments for mu
def plot(f):
  x = np.linspace(0.3, 1, 1000)
  plt.plot(x, (f(2.5, x)).real, "r-")
  plt.plot(x, (f(3, x)).real, "g-")
  plt.plot(x, (f(3.2, x)).real, "b-")
  plt.plot(x, (f(3.5, x)).real, "y-")
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.grid()
  plt.show()

plot(f)