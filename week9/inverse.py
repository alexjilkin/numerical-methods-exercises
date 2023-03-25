import numpy as np
import matplotlib.pyplot as plt
import random

gamma = 1
def e(x):
    return (1/gamma) * np.exp(-(x / gamma))
def lor(x):
    return 1 / (np.pi * (1 + x**2))

def e_inv(y):
    return -gamma * np.log(y)

def lor_inv(y):
    return np.tan(np.pi * (y - 1/2))

nums_e = [e_inv(random.uniform(0, 1)) for _ in range(10**6)]
nums_lor = [lor_inv(random.uniform(0, 1)) for _ in range(10**6)]

M = 1000

# Exponential
plt.hist(nums_e, bins = 1000, density=True)
x = np.linspace(0, 10, M)
plt.plot(x, e(x))

# Lorentz
# plt.hist([x for x in nums_lor if x> -50 and x < 50], bins = M, density=True)
# x = np.linspace(-50, 50, M)
# plt.plot(x, lor(x))

plt.show()