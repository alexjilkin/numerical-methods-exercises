import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, V

import sys
eps = sys.float_info.epsilon

"""
    Plots V(r) as a function of b to find b_max
"""
Z1 = 1
Z2 = 14
Elab = 20

M1 = 1.008 
M2 = 28.085 

bs = np.linspace(eps, 10e-13, 10000)

Vs = []
for b in bs:
    rmin = get_rmin(Z1, Z2, Ecom(Elab), b)
    Vs.append(V(rmin, Z1, Z2))

plt.xlabel('b')
plt.ylabel('V(rmin)')
plt.plot(bs, Vs)
plt.show()