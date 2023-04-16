import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

from numpy import linalg as LA

n = 500
h = 2 / (n - 1)

# Build the differences matrix
D = np.zeros((n, n))
D[0, 0] = -2
D[0, 1] = 1
D[n-1, n-1] = -2
D[n-1, n-2] = 1

for i in range(1, n-1):
    D[i, i-1] = 1
    D[i, i] = -2
    D[i, i+1] = 1

D /= (-2 * (h ** 2))

E, psi = LA.eig(D)

# Sort
i = E.argsort()
E = E[i]
psi = psi[:, i]

x = np.linspace(-1, 1, n)   
# Take by columns and plot first 5
for i in range(0, 5):
    plt.plot(x, psi[:,i], label=f"E{i}={E[i]:.4f}")
plt.legend()
plt.show()

