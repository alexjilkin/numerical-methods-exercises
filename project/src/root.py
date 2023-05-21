import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
"""
This module calculates the distance of minimum approach
"""

""" Alpha and Beta coefficients for the calculation of phi """
alpha = np.array([0.1818, 0.5099, 0.2802, 0.02817])
beta = np.array([3.2, 0.9423, 0.4028, 0.2016])

""" vacuum permittivity and elementary. Without powers of 10 as those are accounted later """
eps_0 = 8.854187817
e = 1.6021892

"""
(e^2 / e_0) coverted to Angstroms 
Also, taking into account 6.242e18 of converting V(r) into eV from Joules
"""
eps_div_e = ((e**2)/eps_0) * 10**2

def phi(x):
    """ phi function (7)
    :x:      variable
    :return: Center of mass energy in Joules
    """
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
    
    res = 0.46848 / ((Z1 ** 0.23) + (Z2 ** 0.23))
    au_dict[key] = res
    
    return res

def V(r, Z1, Z2):
    """ Universal screened Coulomb potential (5)
    :x:      distance
    :Z1:     Atomic number of projectile
    :Z2:     Atomic number of target
    :return: potential in eV
    """
    res = ((Z1 * Z2) / (4 * np.pi * r)) * eps_div_e * phi(r / au(Z1, Z2))

    # Converts to eV from Joules
    return res * 6.242

# Removing the square root as we want to find the root of g(rmin) = 0
def g(r, Z1, Z2, Ecom, b):
    return 1 - ((b / r) ** 2) - (V(r, Z1, Z2) / Ecom)

def Ecom(Elab, M1, M2):
    """Calculates Ecom from Elab and transforms to Joules from eV
    :Elab: Lab energy in eV
    :M1: Atomic mass of projectile
    :M2: Atomic mass of target
    :return: Center of mass energy in Joules
    """
    return (M2 / (M1 + M2)) * Elab

def get_rmin(Z1, Z2, Ecom, b):
    def eq(r):
        return g(r, Z1, Z2, Ecom, b)
    
    res = root(eq, b/2)
    return res.x[0]


def plot():
    """
    Helper function.
    Plots g(r) to get a visual queue of the root
    """
    Z1, M1 = 1, 1.007825  
    Z2, M2 = 14, 28.085 
    b = 0.9
    _, ax = plt.subplots()

    for Elab in np.logspace(1, np.log10(5e6), 10):
        r  = np.linspace(b* 0.1, 10 * b, 1000)
        ax.plot(r, g(r, Z1, Z2, Ecom(Elab, M1, M2), b), label=f"Elab={Elab:.2f}, rmin={get_rmin(Z1, Z2, Ecom(Elab, M1, M2), b):.2f}")
        
    ax.set_xscale('log')
    plt.title(f"b={b:.2f}")
    plt.xlabel('r')
    plt.ylabel('g(r)')
    plt.legend()
    plt.show()

# plot()