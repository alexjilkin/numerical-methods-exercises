import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, g, V
from scipy.integrate import simpson

def F(u, b, rmin, Ecom, Z1, Z2):
    return (b**2 * (2 - u**2) + (rmin**2 / (u**2 * Ecom)) * (V(rmin, Z1, Z2) - V(rmin / (1 - u**2), Z1, Z2))) ** -0.5

def theta(b, Ecom, Z1, Z2 ):
    rmin = get_rmin(Z1, Z2, Ecom, b)
    # print(f"{rmin}, {b}, {Ecom}")
    us = np.linspace(1e-35, 1, 1000)
    return np.pi - 4 * b * simpson([F(u, b, rmin, Ecom, Z1, Z2) for u in us], us)

def Sn(Elab, Z1, Z2):
    E = Ecom(Elab)

    def integ(b):
        return (np.sin(theta(b, E, Z1, Z2) / 2)**2) * b
    
    bs = np.linspace(1e-35, 10e-6, 5000)

    return 2 * np.pi * gamma * Elab * simpson([integ(b) for b in bs], bs)

Z1 = 1
Z2 = 14

M1 = 1.008 
M2 = 28.085 

gamma = (4*M1*M2) / ((M1 + M2) **2)

Elabs = np.logspace(1, 6)
Sns = []
for Elab in Elabs:
    Sns.append(Sn(Elab, Z1, Z2))
   
plt.scatter(Elabs, Sns, s=.4)
plt.show()