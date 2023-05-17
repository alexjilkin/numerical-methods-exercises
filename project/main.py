import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, g, V
from scipy.integrate import simpson

import sys
eps = sys.float_info.epsilon

# Z1 = 1
# Z2 = 14
# M1 = 1.007825  
# M2 = 28.085 

Z1 = 14
M1 = 1.007825  
Z2 = 79
M2 = 196.966570 

def F(u, b, rmin, Ecom, Z1, Z2):
    return (b**2 * (2 - u**2) + (rmin**2 / (u**2 * Ecom)) * (V(rmin, Z1, Z2) - V(rmin / (1 - u**2), Z1, Z2))) ** -0.5

def theta(b, Ecom, Z1, Z2):
    rmin = get_rmin(Z1, Z2, Ecom, b)
    # print(f"{rmin}, {b}, {Ecom}")
    u = np.linspace(eps, 1 - eps, 300)
    y = [F(u, b, rmin, Ecom, Z1, Z2) for u in u]
    return np.pi - 4 * b * simpson(y, u)

def Sn(Elab, Z1, Z2):
    E = Ecom(Elab, M1, M2)

    def integ(b):
        return (np.sin(theta(b, E, Z1, Z2) / 2)**2) * b
    
    b = np.linspace(eps, 10e-7, 600)
    y = [integ(b) for b in b]
    return 2 * np.pi * gamma * Elab * simpson(y, b)

gamma = (4*M1*M2) / (M1 + M2)**2

Elabs = np.logspace(eps, 6, 200)
Sns = []
for Elab in Elabs:
    Sns.append(Sn(Elab, Z1, Z2))
   
plt.loglog(Elabs, Sns)
plt.show()

# print(Sn(5e6, Z1, Z2))