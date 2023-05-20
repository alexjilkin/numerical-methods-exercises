import numpy as np
import matplotlib.pyplot as plt

"""
Calculates and plots the expected values based on fitting a
suitable formula. (14)
"""
def e(Z1, Z2, M1, M2, Elab):
    return (32.53*M2*Elab) /(Z1*Z2 * (M1+M2) * (Z1**0.23 + Z2**0.23))

def Sn(Z1, Z2, M1, M2, Elab):
    return sn(e(Z1, Z2, M1, M2, Elab)) * ((8.462*10e-15*Z1*Z2*M1) / ((M1 + M2)/(Z1**0.23 + Z2**0.23)))

def sn(e):
    return np.where(e <= 30, np.log(1 + 1.138*e) / (2 * (e + 0.01321*e**0.21226 + 0.19593*e**0.5)), np.log(e) / (2*e)) * 10 ** 14

def plot():

    Elab = np.logspace(1, np.log10(5e6), 1000)

    # 1H to 28Si    
    Z1, M1 = 1, 1.007825  
    Z2, M2 = 14, 28.085 
    plt.loglog(Elab, Sn(Z1, Z2, M1, M2, Elab / 1000) * 10**14, label="1H to 28Si")

    # 28Si to 197Au
    Z1, M1  = 14, 1.007825
    Z2, M2 = 79, 196.966570 
    plt.loglog(Elab, Sn(Z1, Z2, M1, M2, Elab / 1000) * 10**14, label="28Si to 197Au")

    plt.show()

# plot()