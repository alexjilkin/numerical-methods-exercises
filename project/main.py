import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, V
from scipy.integrate import simpson

from expected import Sn as Sn_expected
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

u_space = np.linspace(eps, 1 - eps, 1000)
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

b_max = 4
b_space = np.linspace(eps, b_max, 1000)
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


materials = [
    # 1H to 28Si 
    ((1, 1.007825), (14, 28.085 )),
    # 28Si to 197Au
    ((14, 1.007825), (79, 196.966570))
]

for projectile, target in materials:
    Z1, M1 = projectile
    Z2, M2 = target

    Elab = np.logspace(1, np.log10(5e6), 300)

    # Plots a log-log of numerical Sn and expected Sn with mean squared error
    y = [Sn(E, Z1, Z2, M1, M2) for E in Elab]
    y_expected = Sn_expected(Z1, Z2, M1, M2, Elab / 1000)
    plt.loglog(Elab,y , label=f"ZBL:(Z1={Z1}, M1={M1}), (Z2={Z2}, M2={M2})")
    mse = np.square(y - y_expected).mean() 
    plt.loglog(Elab, y_expected, label=f"Expected:(Z1={Z1}, M1={M1}), (Z2={Z2}, M2={M2}) mse={mse}")
    
    print()
plt.xlabel('Elab')
plt.ylabel('Sn(Elab)')

plt.legend()
plt.show()

