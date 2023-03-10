import numpy as np
import matplotlib.pyplot as plt
import time 

tr_pi = (3 * np.pi)

# f and g functions and their derivatives (prime) from the exercise
def f(x):
  return np.sin((tr_pi * x**3) / (x**2 - 1)) + 1/2
def g(x, B):
  return x + np.exp((-B) * x**2) * np.cos(x)
def g_prime(x, B):
  return 1 + np.exp((-B) * x**2) * ((-2* B * x)* np.cos(x) - np.sin(x))

def f_prime(x):
  return (tr_pi * np.cos((tr_pi * x**3) / (x**2 - 1)) * (x**4 - 3*(x**2))) / ((x**2 - 1)* (x**2 - 1))

tol = 0.00001

# Finds root of f using the bisection method
def bisect_f(a, b):
  if (b - a <= tol):
    return a
    
  m = 0.5 * (a + b)
  f_m = f(m)
  if (np.abs(f_m) <= tol):
    return m

  f_a = f(a)
  return bisect_f(a, m) if f_m * f_a < 0 else bisect_f(m, b)

# Finds root of f using Newton's method
def newton_f(x0):
  x_i = x0 - (f(x0) / f_prime(x0))
  
  if (np.abs(f(x_i)) < tol):
    return x_i

  return newton_f(x_i)

# Finds root of g using newton's method
def newton_g(x0, B):
  x_i = x0 - (g(x0, B) / g_prime(x0, B))
  
  if (np.abs(g(x_i,B)) < tol):
    return x_i

  return newton_g(x_i, B)

# Plots the given function as argument
def plot(f):
  x = np.linspace(-2, 2, 1000)
  plt.plot(x, f(x))
  
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.grid()
  plt.show()

# Runs both root finding functions are calculates the time it takes
def test_both():
  st = time.time()
  x = bisect_f(0, 1)
  bisect_et = time.time()
  print("The bisection root is: {}, which evaluates f(x)={} \n it took it {}s to evaluate".format(x, f(x), bisect_et - st))

  st = time.time()
  x = newton_f(0.3)
  newton_et = time.time()
  print("The newton root is: {}, which evaluates f(x)={} \n it took it {}s to evaluate".format(x, f(x), newton_et - st))


# Prints a test for g(x)
def test_g(B):
  x = newton_g(-0.1, B)
  print(x)
  print(g(x,B))
  print("The newton root is: {}, which evaluates g(x)={} \n ".format(x, f(x)))
  plot(lambda x: g(x, B))


#test_both()
# plot(f)
# test_g(100)
