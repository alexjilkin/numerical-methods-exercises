import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

from numpy import linalg as LA

n = 201
dx = 2 / n

# Build the differences array
D = np.zeros((n, n))
for i in range(1, n-1):
    D[i, i-1] = 1
    D[i, i] = -2 * dx
    D[i, i+1] = 1
    

w, psi = LA.eig(D)

# En = 0.5 * (2 * np.pi * np.arange(5)) ** 2
# print(w, En)

x = np.linspace(-1, 1, n)
# Take by columns
plt.plot(x, psi[:, 0])
plt.plot(x, psi[:, 1])
plt.show()

