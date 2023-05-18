import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, g, V
from scipy.integrate import simpson

eps = np.finfo(float).eps

# 1H to 28Si    
Z1, M1 = 1, 1.007825  
Z2, M2 = 14, 28.085 

# # 28Si to 197Au
# Z1, M1  = 14, 1.007825
# Z2, M2 = 79, 196.966570 

def F(u, b, rmin, Ecom, Z1, Z2):
    return (b**2 * (2 - u**2) + (rmin**2 / (u**2 * Ecom)) * (V(rmin, Z1, Z2) - V(rmin / (1 - u**2), Z1, Z2))) ** -0.5

u_space = np.linspace(eps, 1 - eps, 500)
def theta(b, Ecom, Z1, Z2):
    rmin = get_rmin(Z1, Z2, Ecom, b)
   
    y = F(u_space, b, rmin, Ecom, Z1, Z2)
    return np.pi - 4 * b * simpson(y, u_space)

b_space = np.linspace(eps, 10e-7, 500)
def Sn(Elab, Z1, Z2):
    E = Ecom(Elab, M1, M2)

    def integ(b):
        return (np.sin(theta(b, E, Z1, Z2) / 2)**2) * b
    
    y = [integ(b) for b in b_space]
    return 2 * np.pi * gamma * Elab * simpson(y, b_space)

gamma = (4*M1*M2) / (M1 + M2)**2

Elab = np.logspace(np.log10(5), np.log10(5e6), 300)
Sn_res = []
for E in Elab:
    Sn_res.append(Sn(E, Z1, Z2))

# Plots a log-log 
plt.loglog(Elab, Sn_res)
plt.xlabel('Elab')
plt.ylabel('Sn(Elab)')
plt.show()

# print(Sn(5e6, Z1, Z2))