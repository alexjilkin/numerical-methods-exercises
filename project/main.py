import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, V
from scipy.integrate import simpson

eps = np.finfo(float).eps

# 1H to 28Si    
Z1, M1 = 1, 1.007825  
Z2, M2 = 14, 28.085 

# 28Si to 197Au
# Z1, M1  = 14, 1.007825
# Z2, M2 = 79, 196.966570 

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

u_space = np.linspace(eps, 1 - eps, 300)
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

b_max = 10
b_space = np.linspace(eps, b_max, 300)
def Sn(Elab, Z1, Z2):
    """Calculates the stopping power of projectile Z1 into matter Z2 with energy Elab
    :Elab:   eV Energy in laboratory coordinate system
    :Z1:     Atomic number of projectile
    :Z2:     Atomic number of target
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

Elab = np.logspace(1, np.log10(5e6), 150)
Sn_res = []
for E in Elab:
    Sn_res.append(Sn(E, Z1, Z2))

# Plots a log-log 
plt.loglog(Elab, Sn_res)
plt.xlabel('Elab')
plt.ylabel('Sn(Elab)')
plt.show()
