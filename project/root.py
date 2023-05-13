import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, elementary_charge
from scipy.optimize import root

alpha = np.array([0.1818, 0.5099, 0.2802, 0.02817])
beta = np.array([3.2, 0.9423, 0.4028, 0.2016])

def phi(x):
    sum = 0
    for i in range(4):
        sum += alpha[i] * np.exp(-beta[i]*x)

    return sum 

def a_u(Z1, Z2):
    return 0.46848e-10 / ((Z1 ** 0.23) + (Z2 ** 0.23))

def V(r, Z1, Z2):
    return ((Z1 * Z2 * (elementary_charge ** 2)) / (4 * np.pi * epsilon_0 * r)) * phi(r / a_u(Z1, Z2))

def g(r, Z1, Z2, Ecom, b):
    return (1 - ((b / r) ** 2) - (V(r, Z1, Z2) / Ecom))

M1 = 1.008 
M2 = 28.085 

Elab = 20
def Ecom(Elab):
    return (M2 / (M1 + M2)) * Elab * 1.60218e-19

b = 5e-12

def get_rmin(Z1, Z2, Ecom, b):
    def eq(args):
        r = args[0]
        return [g(r, Z1, Z2, Ecom, b)]
    
    res = root(eq, b)
    return res.x[0]

# r  = np.linspace(b* 0.1, 10e2 * b, 10000)
# fig, ax = plt.subplots()

# ax.plot(r, g(r, Z1, Z2, Ecom, b), label=f"b={b}, r=[0, {r.max()}], Elab={Elab}")

# ax.set_xscale('log')
# plt.xlabel('r')
# plt.ylabel('g(r)')
# plt.legend()
# plt.show()
