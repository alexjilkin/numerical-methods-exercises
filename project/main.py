import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0
from scipy.optimize import root

alpha = np.array([0.1818, 0.5099, 0.2802, 0.02817])
beta = np.array([3.2, 0.9423, 0.4028, 0.2016])

def phi(x):
    return np.sum(alpha + np.exp(-beta*x))

def a_u(Z1, Z2):
    return (0.46848) / (Z1 ** 0.23 + Z2 ** 0.23)

def V(r, Z1, Z2):
    return ((Z1 * Z2) / (4 * np.pi * epsilon_0 * r)) * phi(r / a_u(Z1, Z2))

def g(r, Z1, Z2, Ecom, b):
    return np.sqrt(1 - ((b / r) ** 2) - (V(r, Z1, Z2) / Ecom))

def get_rmin(Z1, Z2, Ecom, b):
    return root(lambda r: g(r, Z1, Z2, Ecom, b), 4)

Z1 = 1
Z2 = 14

M1 = 1.008 
M2 = 27.9769
Elab = 5
Ecom = (M2 / (M1 + M2)) * Elab

b = 10 ** -20

rmin = get_rmin(Z1, Z2, Ecom, b)
print(rmin)