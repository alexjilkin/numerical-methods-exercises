import sys
sys.path.append('./')

import numpy as np
from src.root import get_rmin, Ecom, V
from scipy.integrate import simpson

# Machine epsilon
eps = np.finfo(float).eps

def F(u, b, rmin, Ecom, Z1, Z2):
    """F function defined after variable substitution
    :u:      substitute variable
    :b:      collision parameter
    :rmin:   distance of minimum approach
    :Ecom:   eV Energy in center of mass system
    :Z1:     Atomic number of projectile
    :Z2:     Atomic number of target
    :return: Theta function value
    """
    res = ((b**2 * (2 - u**2)) + (rmin**2 / (u**2 * Ecom)) * (V(rmin, Z1, Z2) - V(rmin / (1 - u**2), Z1, Z2)))

    return 1 / np.sqrt(res)

u_space = np.linspace(eps, 1 - eps, 200)
def theta(b, Ecom, Z1, Z2):
    """Theta function
    :b:      collision parameter
    :Ecom:   eV Energy in center of mass system
    :Z1:     Atomic number of projectile
    :Z2:     Atomic number of target
    :return: Theta function value
    """
    rmin = get_rmin(Z1, Z2, Ecom, b)
   
    y = F(u_space, b, rmin, Ecom, Z1, Z2)
    return np.pi - 4 * b * simpson(y, u_space)

# Static b_max from negligible potential calculations
b_max = 4
b_space = np.linspace(eps, b_max, 200)
def Sn(Elab, Z1, Z2, M1, M2):
    """Calculates the stopping power of projectile Z1 into matter Z2 with energy Elab
    :Elab:   eV Energy in laboratory coordinate system
    :Z1:     Atomic number of projectile
    :Z2:     Atomic number of target
    :M1:     Atomic mass of projectile
    :M2:     Atomic mass of target
    :return: Stopping power
    """
    E = Ecom(Elab, M1, M2)
    
    y = [(np.sin(theta(b, E, Z1, Z2) / 2)**2) * b for b in b_space]
    return 2 * np.pi * gamma(M1, M2) * Elab * simpson(y, b_space)

def gamma(M1, M2):
    """Returns the Gamma of M1 and M2
    :M2:     Atomic mass of projectile
    :M2:     Atomic mass of target
    :return: Gamma
    """
    return (4*M1*M2) / ((M1+M2)**2)