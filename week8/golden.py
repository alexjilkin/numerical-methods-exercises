import numpy as np
from scipy.special import erfc
from scipy.optimize import golden as scipy_golden
import matplotlib.pyplot as plt

def f(x):
    return ((x**4) * erfc(x)) - np.sin(x)

golden_ratio = (1 + np.sqrt(5)) / 2
lim = 1e-5

def golden(xa, xc):
  one = xc - (xc - xa) / golden_ratio
  two = xa + (xc - xa) / golden_ratio
  
  while np.abs(xc - xa) > lim:
    if f(one) < f(two): 
        xc = two
    else:
        xa = one

    delt = (xc - xa) / golden_ratio
    one = xc - delt
    two = xa + delt

  return (xc + xa) / 2


print(golden(-200, 200))

print(scipy_golden(f, brack=(0, 100)))
space = np.linspace(-1000, 1000, 1000)
plt.plot(space, f(space))
plt.show()