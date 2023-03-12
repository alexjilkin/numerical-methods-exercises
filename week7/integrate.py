import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return np.exp(-x) * (np.cos(x) ** 2)
def f_sub(t):
    return (np.exp(-t/(1-t)) * (np.cos(t/(1-t)) ** 2)) / ((1-t) ** 2)

def simpson(f, a, b, eps, level, level_max):
  h = b - a
  c = 0.5 * (a + b)
  one_simpson = h * (f(a)+4.0*f(c)+f(b)) / 6.0
  d = 0.5*(a+c); e = 0.5*(c+b);
  two_simpson = h * (f(a)+4.0*f(d)+2.0*f(c)+4.0*f(e)+f(b))/12.0;

  if (level + 1 >= level_max):
    result = two_simpson;
    print("Maximum level reached\n")
    return result
  
  if (np.abs(two_simpson - one_simpson) < 15.0 * eps):
    result = two_simpson + (two_simpson-one_simpson)/15.0;
  else:
    left_simpson = simpson(f, a, c, eps / 2, level + 1, level_max);
    right_simpson = simpson(f, c, b , eps / 2,level + 1, level_max);
    result = left_simpson + right_simpson;
  
  return result
eps = 10e-5

print("Expected result using scipy I={}".format(quad(f, 0, 10e+3)))
print("Simpons and truncating I={}".format(simpson(f, 0, 20, eps , 0, 10)))
print("Simpons and substituion I={}".format(simpson(f_sub, 0, 1 - eps, eps, 0, 10)))

# plt.plot(np.linspace(0, 50, 100), f(np.linspace(0, 50, 100)))
# plt.show()