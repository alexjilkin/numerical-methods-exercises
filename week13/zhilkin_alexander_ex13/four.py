import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# Reads from the file and creats a matrix with two columns
fileName = "ex13p4_d3.dat"
with open(f"./data/{fileName}") as f:
    lines = f.readlines()
samples = np.array([list(map(lambda n: float(n), line.strip().split())) for line in lines])

# Function to fit, getting [a, b] as args. A Maxwell–Boltzmann distribution
def func(v, args):
    a, b = args
    return a * (v**2) * np.exp(-(v**2) / (2*b))

# Gets the result by least squares method
params0 = [0, 10000]
res = least_squares(lambda params: func(samples[:, 0], params) - samples[:, 1], params0, method='lm')

if (res.success != True):
    print("Failed to fit")

# Plots the original data
plt.plot(samples[:, 0], samples[:, 1], label=fileName)

a, b = res.x
# Plots fitted function
plt.plot(samples[:, 0], func(samples[:, 0], res.x), label=f"a={a:.3f}, b={b:.3f}")
plt.title(fileName)
plt.legend()
plt.show()
