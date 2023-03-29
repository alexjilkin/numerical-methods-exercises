import numpy as np
import matplotlib.pyplot as plt
import random

# Returns value of pi using a hit and miss with N samples scheme for the unit circle
def mypi(N):
  accepted = 0

  for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if ((x**2 + y**2) <= 1):
      accepted += 1

  return (4 * accepted) / (accepted + (N - accepted))

# Returns value of pi using a hit and miss with N samples scheme for the unit sphere
def mypi_sphere(N):
  accepted = 0

  for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    z = random.uniform(-1, 1)

    if ((x**2 + y**2 + z**2) <= 1):
      accepted += 1

  return (6 * accepted) / (accepted + (N - accepted))

# Plots an histogram for different Ns for 1000 experiments
def pi_hist():
  Ns = [10**2, 10**3, 10**4]

  for N in Ns:
    pi_array = np.array([mypi(N) for _ in range(1000)])
    print("N={} pi_mean={}".format(N, pi_array.mean()))
    plt.hist(pi_array, density=True, bins=30, label="N={}".format(N))

  plt.axvline(np.pi, color='r', linestyle='--')
  plt.plot(np.pi, 2 , 'r*')
  plt.legend()
  plt.show()

pi_hist()