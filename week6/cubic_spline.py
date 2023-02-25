import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

Ns = [5, 10, 20]
deriv_values = [0, 1, 10]

# Plots cubic spline interpolation for each N and derivative value
for N in Ns:
  x = np.arange(N)
  y = np.random.uniform(size=N)

  for deriv_value in deriv_values:
    # CubicSpline accepts a tuple of tuples of start and end derivatives
    cs = CubicSpline(x, y, bc_type=((2, deriv_value), (2, deriv_value)))
    xs = np.arange(0, N, 0.1)

    plt.plot(xs, cs(xs), label="N={}, S''={}".format(N, deriv_value))

plt.legend()

plt.show()
