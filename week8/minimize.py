import numpy as np
from scipy.special import erfc
from scipy.optimize import minimize as sp_minimize, fmin_powell
import time

import matplotlib.pyplot as plt

def f(args):
  x, y = args
  return 7*np.exp(-((x - 2)**2)) + 3*(x**2) + (2*x*y) + (5*(y**2)) - 8 * np.exp(-((y+4)**2))
  
# Minimizes f, with x0 and y0 as initial guesses.
# algo=1,2,3,4 for Nelder-Mead, fmin_powell, conjugate gradients, Broyden–Fletcher–Goldfarb–Shanno algorithsm respectively.
def minimize(x0, y0, alg):
  method = ""
  match alg:
    case 1:
      method = "Nelder-Mead"
    case 2:
       return fmin_powell(f, [x0, y0])
    case 3:
      method = "CG"
    case 4:
      method = "BFGS"

  res = sp_minimize(f, [x0, y0], method=method)
  if (res.success):
    return res.x
  else:
    ValueError(res.message)

# A wrapper for minimize to also return runtime
def minimize_with_perf(*argv):
  st = time.time()
  res = minimize(*argv)
  et = time.time()
  
  return (res, et - st)

def plot_f():
  x = np.linspace(-10, 10, 100)
  y = np.linspace(-10, 10, 100)
  X, Y = np.meshgrid(x, y)

  # Evaluate the function over the meshgrid
  Z = f((X, Y))

  # Plot the function
  fig = plt.figure(figsize=(10,8))
  ax = plt.axes(projection="3d")
  ax.plot_surface(X, Y, Z, cmap='viridis')
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('f(x,y)')
  plt.show()

x0 = 2
y0 = -4
print("Nelder-Mean: {} \nPowell's: {} \nCG: {} \nBFGS: {}".format(minimize_with_perf(x0, y0, 1), minimize_with_perf(x0, y0, 2), minimize_with_perf(x0, y0, 3), minimize_with_perf(x0, y0, 4)))
# plot_f()