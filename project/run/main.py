import sys
sys.path.append('../')

import numpy as np
import matplotlib.pyplot as plt
from src.stopping_power import Sn 
from src.expected import Sn as Sn_expected
""" 
The materials to test
Each member of the array is a tuple of atomic (number, mass)
"""
materials = [
    # 1H to 28Si 
    ((1, 1.007825), (14, 28.085 )),
    # 28Si to 197Au
    ((14, 1.007825), (79, 196.966570))
]

# Plots a log-log of numerical Sn and expected Sn with mean squared error
for projectile, target in materials:
    Z1, M1 = projectile
    Z2, M2 = target

    Elab = np.logspace(1, np.log10(5e6), 200)
    y = np.array([Sn(E, Z1, Z2, M1, M2) for E in Elab])

    # Exected stopping power from universial equation. Receives energy in KeV
    y_expected = Sn_expected(Z1, Z2, M1, M2, Elab / 1000)

    # Mean squared error between the ZBL model calculation and universal equation "expected" value
    mse = np.square(y - y_expected).mean() 

    plt.loglog(Elab,y , label=f"ZBL:(Z1={Z1}, M1={M1}) -> (Z2={Z2}, M2={M2})")
    plt.loglog(Elab, y_expected, label=f"Exp:(Z1={Z1}, M1={M1}) -> (Z2={Z2}, M2={M2}) mse={mse:.2f}")
    
plt.xlabel('Elab')
plt.ylabel('Sn(Elab)')
plt.legend()
plt.show()