import numpy as np
from root import get_rmin, Ecom, g, V
from scipy.integrate import quad

def F(u, b, rmin, Ecom, Z1, Z2):
    return (b**2 * (2 - u)**2 + (rmin**2 / (u**2 * Ecom)) * (V(rmin, Z1, Z2) - V(rmin / (1 - u**2), Z1, Z2))) ** -0.5

def theta( b, rmin, Ecom, Z1, Z2 ):
    return np.pi - 4 * b * quad(lambda u: F(u, b, rmin, Ecom, Z1, Z2), 0, 1)[0]

def Sn(b, rmin, Ecom, Z1, Z2):
    return 2 * np.pi * gamma * Elab * theta(b, rmin, Ecom, Z1, Z2)

Z1 = 1
Z2 = 14

M1 = 1.008 
M2 = 28.085 

Elab = 10000
b = 5e-12

gamma = (4*M1*M2) / ((M1 + M2) **2)

rmin = get_rmin(Z1, Z2, Ecom(Elab), b)
print(f"rmin={rmin}")
print(f"g(rmin)={g(rmin, Z1, Z2, Ecom(Elab), b)}")


print(theta(b, rmin, Ecom(Elab), Z1, Z2))
# r  = np.linspace(b* 0.1, 10e2 * b, 10000)
# fig, ax = plt.subplots()

# ax.plot(r, g(r, Z1, Z2, Ecom, b), label=f"b={b}, r=[0, {r.max()}], Elab={Elab}")

# ax.set_xscale('log')
# plt.xlabel('r')
# plt.ylabel('g(r)')
# plt.legend()
# plt.show()
