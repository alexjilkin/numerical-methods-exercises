import numpy as np
import matplotlib.pyplot as plt
from root import get_rmin, Ecom, V

import sys
eps = sys.float_info.epsilon

""" Plots V(r) as a function of b to find b_max """

# 1H to 28Si    
Z1, M1 = 1, 1.007825  
Z2, M2 = 14, 28.085 

# 28Si to 197Au
Z1, M1  = 14, 1.007825
Z2, M2 = 79, 196.966570 

Elab = 10

bs = np.linspace(eps, 5, 1000)

Vs = []
for b in bs:
    rmin = get_rmin(Z1, Z2, Ecom(Elab, M1, M2), b)
    Vs.append(V(rmin, Z1, Z2))

plt.xlabel('b')
plt.ylabel('V(rmin)')
plt.plot(bs, Vs)
plt.show()