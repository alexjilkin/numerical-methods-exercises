import numpy as np
import math

tr_pi = (3 * np.pi)

def f(x):
  return np.sin((tr_pi * x**3) / (x**2 - 1)) + 1/2

def f_prime(x):
  return (tr_pi * np.cos((tr_pi * x**3) / (x**2 - 1)) * (x**4 - 3*(x**2))) / ((x**2 - 1)* (x**2 - 1))

tol = 0.00001

def bisect_f(a, b):
  if (b - a <= tol):
    return a
    
  m = 0.5 * (a + b)
  f_m = f(m)
  if (np.abs(f_m) <= tol):
    return m

  f_a = f(a)
  return bisect_f(a, m) if f_m * f_a < 0 else bisect_f(m, b)

def newton_f(x0):
  x_i = x0 - (f(x0) / f_prime(x0))
  
  if (np.abs(f(x_i)) < tol):
    return x_i

  return newton_f(x_i)

x = bisect_f(-0.5, 0.5)
print(x)
print(f(x))

x = newton_f(0.2)
print(x)
print(f(x))

