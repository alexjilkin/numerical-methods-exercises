import numpy as np
import matplotlib.pyplot as plt

def e(Z1, Z2, M1, M2, Elab):
    return (32.53*M2*Elab) /(Z1*Z2*(M1 + M2)*(Z1**0.23 + Z2**0.23))

def Sn(Z1, Z2, M1, M2, Elab):
    return sn(e(Z1, Z2, M1, M2, Elab))*((8.462*10e-15*Z1*Z2*M1)/((M1 + M2)/(Z1**0.23 + Z2**0.23)))

def sn(e):
    if (e <= 30):
        return np.log(1 + 1.138*e) / (2 * (e + 0.01321*e**0.21226 + 0.19593*e**0.5))
    else:
        return np.log(e) / (2*e)

# 1H to 28Si    
Z1, M1 = 1, 1.007825  
Z2, M2 = 14, 28.085 

# # 28Si to 197Au
# Z1, M1  = 14, 1.007825
# Z2, M2 = 79, 196.966570 

Elab = np.logspace(1, np.log10(5e6), 10000)

Sns = []
for E in Elab:
    # Energy converted to KeV
    Sns.append(Sn(Z1, Z2, M1, M2, E / 1000) * 10**14)

plt.loglog(Elab, Sns)
plt.show()
