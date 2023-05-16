import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, g, V
from scipy.integrate import quad

def F(u, b, rmin, Ecom, Z1, Z2):
    return (b**2 * (2 - u**2) + (rmin**2 / (u**2 * Ecom)) * (V(rmin, Z1, Z2) - V(rmin / (1 - u**2), Z1, Z2))) ** -0.5

def theta(b, Ecom, Z1, Z2 ):
    rmin = get_rmin(Z1, Z2, Ecom, b)
    print(f"{rmin}, {b}, {Ecom}")
    return np.pi - 4 * b * quad(lambda u: F(u, b, rmin, Ecom, Z1, Z2), 0, 1)[0]

def Sn(Ecom, Z1, Z2):
    def integ(b):
        return (np.sin(theta(b, Ecom, Z1, Z2) / 2)**2) * b
    
    return 2 * np.pi * gamma * Elab * quad(integ, 0, 0.01)[0]

Z1 = 1
Z2 = 14

M1 = 1.008 
M2 = 28.085 

b = 5e-12

gamma = (4*M1*M2) / ((M1 + M2) **2)

Elabs = np.logspace(1, 2, 20)
Sns = []
for Elab in Elabs:
    Sns.append(Sn(Ecom(Elab), Z1, Z2))
   
plt.scatter(Elabs, Sns, s=1)
plt.show()

# r  = np.linspace(b* 0.1, 10e2 * b, 10000)
# fig, ax = plt.subplots()

# ax.plot(r, g(r, Z1, Z2, Ecom, b), label=f"b={b}, r=[0, {r.max()}], Elab={Elab}")

# ax.set_xscale('log')
# plt.xlabel('r')
# plt.ylabel('g(r)')
# plt.legend()
# plt.show()
