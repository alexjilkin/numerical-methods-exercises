import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, elementary_charge
from root import get_rmin, Ecom, g

Z1 = 1
Z2 = 14

M1 = 1.008 
M2 = 28.085 

Elab = 20
b = 5e-12

gamma = (4*M1*M2) / ((M1 + M2) **2)

def theta(rmin, Ecom):
    return Ecom

def Sn(Elab, rmin):
    return 2 * np.pi * gamma * Elab * theta(rmin, Ecom(Elab))

rmin = get_rmin(Z1, Z2, Ecom(Elab), b)
print(f"rmin={rmin}")
print(f"g(rmin)={g(rmin, Z1, Z2, Ecom(Elab), b)}")

# r  = np.linspace(b* 0.1, 10e2 * b, 10000)
# fig, ax = plt.subplots()

# ax.plot(r, g(r, Z1, Z2, Ecom, b), label=f"b={b}, r=[0, {r.max()}], Elab={Elab}")

# ax.set_xscale('log')
# plt.xlabel('r')
# plt.ylabel('g(r)')
# plt.legend()
# plt.show()
