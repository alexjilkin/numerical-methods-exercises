import numpy as np
from scipy import optimize

def f1(x):
  return np.exp(-(x[0]**2 + x[1]**2 )) - 1/8
def f2(x):
  return np.sin(x[0]) - np.cos(x[1])

def f(x):
  return np.array([f1(x), f2(x)])

def f_lin(x):
  return f1(x), f2(x)

def broyden(x_init):
  x = x_init
  fx = f(x)
  B = np.identity(len(x))
  
  for i in range(1000):
    s = np.linalg.solve(B, -fx)
    x_new = x + s
    fx_new = f(x_new)
    y = fx_new - fx
    B = B + np.outer((y - np.dot(B, s)), s) / np.dot(s, s)
    
    if np.linalg.norm(fx_new) < 1e-6:
        return x_new

    x = x_new
    fx = fx_new
      
  return x

print(broyden(np.array([2, 2])))

print(optimize.broyden1(f_lin, [1,1]))