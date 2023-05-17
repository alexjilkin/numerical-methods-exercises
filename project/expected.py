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
    
Z1 = 1
Z2 = 14
M1 = 1.007825  
M2 = 28.085 

# Z1 = 14
# M1 = 1.007825  

# Z2 = 79
# M2 = 197

Elabs = np.logspace(0, 6, 1000)

Sns = []
for Elab in Elabs:
    Sns.append(Sn(Z1, Z2, M1, M2, Elab / 1000))

plt.loglog(Elabs, Sns)
plt.show()
