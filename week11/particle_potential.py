import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

from numpy import linalg as LA


def solve_psi(n, v0):
    h = 2 / (n - 1)

    # Build the differences matrix
    D = np.zeros((n, n))
    D[0, 0] = -2
    D[1, 2] = 1

    D[n-1, n-1] = -2
    D[n-1, n-2] = 1

    for i in range(1, n-1):
        D[i, i-1] = 1
        D[i, i] = -2 - (v0 * 2 * h**2 * i*h*(2 - (i*h)))
        D[i, i+1] = 1

    D /= (-2 * (h ** 2))

    E, psi = LA.eig(D)

    # Sort
    i = E.argsort()
    E = E[i]
    psi = psi[:, i]

    return E, psi

# Calculates the estimated E with perturbation theory
def pert_E(n, v0):
    # Solve psi for V0=0
    E, psi = solve_psi(n, 0)
    E0 = E[0]
    psi0 = psi[:, 0]

    # Nominator from perturbation theory equation
    def nominator(psi0):
        return [(psi0[i] ** 2) * v0 * (1 - (-1 + (2 * (i / (n - 1))))**2) for i in np.arange(0, n)]

    # Denominator from perturbation theory equation
    def denominator(psi0):
        return psi0 ** 2

    # Solves integral
    return E0 + (np.trapz(nominator(psi0), dx=2/n) / np.trapz(denominator(psi0), dx=2/n))

n = 1000

v0s = [1, 10, 30]
for v0 in v0s:
    E, psi = solve_psi(n, v0)
    print(f"V0={v0}, E0={E[0]}")
    print(pert_E(n, v0))


