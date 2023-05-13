import numpy as np
from scipy.optimize import root

def f(x, a):
    return x**2 - a

a = 5
x0 = 1

sol = root(f, x0, args=(a,))
print(sol.x)