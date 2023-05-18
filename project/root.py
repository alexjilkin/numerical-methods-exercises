import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from scipy.optimize import root

alpha = np.array([0.1818, 0.5099, 0.2802, 0.02817])
beta = np.array([3.2, 0.9423, 0.4028, 0.2016])

# Convert m^-2 to cm^-2
eps_0 = constants.epsilon_0 * (10**-4)
e = constants.elementary_charge

def phi(x):
    sum = 0
    for i in range(4):
        sum += alpha[i] * np.exp(-beta[i]*x)

    return sum

au_dict = {}

def au(Z1, Z2):
    """Calculates the screening length of Z1 and Z2 atomic numbers
    memoizes the result with Z1-Z2 as key
    :Z1: Atomic number of projectile
    :Z2: Atomic number of target
    :return: Center of mass energy in Joules
    """
    key = f"{Z1}-{Z2}"
    if (key in au_dict):
        return au_dict[key]
    
    # Converts angstroms to cm
    res = 0.46848e-8 / ((Z1 ** 0.23) + (Z2 ** 0.23))
    au_dict[key] = res
    
    return res

def V(r, Z1, Z2):
    res = ((Z1 * Z2 * (e ** 2)) / (4 * np.pi * eps_0 * r)) * phi(r / au(Z1, Z2))

    # Converts to eV from Joules
    return res * 6.242e+18

def g(r, Z1, Z2, Ecom, b):
    return (1 - ((b / r) ** 2) - (V(r, Z1, Z2) / Ecom))

# 
# 
def Ecom(Elab, M1, M2):
    """Calculates Ecom from Elab and transforms to Joules from eV
    :Elab: Lab energy in eV
    :M1: Atomic mass of projectile
    :M2: Atomic mass of target
    :return: Center of mass energy in Joules
    """
    return (M2 / (M1 + M2)) * Elab

def get_rmin(Z1, Z2, Ecom, b):
    def eq(args):
        r = args[0]
        return [g(r, Z1, Z2, Ecom, b)]
    
    res = root(eq, b)
    return res.x[0]

def plot():
    Z1 = 1
    Z2 = 14
    M1 = 1.008 
    M2 = 28.085 
    b = 1e-10
    Elab = 2

    r  = np.linspace(b* 0.1, 10e2 * b, 10000)
    fig, ax = plt.subplots()

    ax.plot(r, g(r, Z1, Z2, Ecom(Elab, M1, M2), b), label=f"b={b}, r=[0, {r.max()}], Elab={Elab}, rmin={get_rmin(Z1, Z2, Ecom(Elab, M1, M2), b)}")

    ax.set_xscale('log')
    plt.xlabel('r')
    plt.ylabel('g(r)')
    plt.legend()
    plt.show()

# plot()