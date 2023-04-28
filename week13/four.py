import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

with open('./data/ex13p4_d1.dat') as f:
    lines = f.readlines()

samples = np.array([list(map(lambda n: float(n), line.strip().split())) for line in lines])

def func(v, args):
    a, b = args
    
    return a * (v**2) * np.exp(-(v**2) / (2*b))

def obj_func(args):
    return func(samples[:, 0], args) - samples[:, 1]

args0 = [500, 500]
res = least_squares(obj_func, args0, method='lm')

print(res)

plt.plot(samples[:, 0], samples[:, 1])

plt.plot(samples[:, 0], func(samples[:, 0], res.x))
plt.show()
