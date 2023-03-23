import numpy as np
import matplotlib.pyplot as plt
import random

def mypi(N):
  accepted = 0

  for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if ((x**2 + y**2) <= 1):
      accepted += 1

  return (4 * accepted) / (accepted + (N - accepted))

Ns = [10**2, 10**3, 10**4]

for N in Ns:

  pi_array = [mypi(N) for _ in range(1000)]

  plt.hist(pi_array, density=True, bins=30, label="N={}".format(N))

plt.axvline(np.pi, color='r', linestyle='--')
plt.plot(np.pi, 2 , 'r*')
plt.legend()
plt.show()
