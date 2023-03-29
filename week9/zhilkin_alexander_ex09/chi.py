import numpy as np
import matplotlib.pyplot as plt
import random 

# Returns chi^2 value based on the N = amount of random numbers; M = number of bins
def get_chi(N, M):
  rand = random.random
  bin_size = 1 / M
  bins = [[] for i in range(M)]

  # Create N random numbers and puts them in bins
  for _ in range(0, N):
    num = rand()
    bin_index = int(np.floor(num / bin_size))

    bins[bin_index].append(num)

  # Size of bins
  y = np.array([len(a) for a in bins])
  E = N / M

  chi_arr = ((y - E)**2) / E
  chi = np.sum(chi_arr)
  return chi

# Prints the chi mean, median. Then plots a distribution of those.
# With N random numbers into M bins
def chi_mean_hist(N, M):
  chis_array = np.array([get_chi(N, M) for i in range(0, 50000)])

  print("Mean: {}, Median: {}".format(np.mean(chis_array), np.median(chis_array)))

  plt.hist(chis_array, bins=50)
  plt.show()

chi_mean_hist(100, 10)
