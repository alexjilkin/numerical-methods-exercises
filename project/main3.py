import numpy as np
from scipy.integrate import quad

alpha_0 = 0.1
beta = np.sqrt(10)
def alpha(i):
    alpha_0 * (beta ** (i - 1))

N = 25

def V(r):
    return -(1/r)

def R(al, r):
    return N * (r ** l) * np.exp(-al * (r ** 2))

def T(al, bet, l):
    def T_int1(r):
        return (r ** 2) * (r ** (2 * l - 1)) * np.exp(r * r * (-al - bet)) * (l - 2*al*r) * (l - 2*bet*r)
    def T_int2(r):
        return R(al, r) * R(bet, r)

    return 0.5 * (N * N * quad(T_int1, 0, np.inf)[0] + l * (l+1) * quad(T_int2, 0, np.inf)[0])

def V(al, bet, l):
    def V_int(r):
        return np.exp(r * r * (-al - bet)) * (r ** (2*l +1))
    
    return -N * N * quad(V_int, 0, np.inf)[0]

def S(al, bet, l):
    return N * N * quad(lambda r: r ** (2 * l) * np.exp(r * r * (-al - bet)), 0, np.inf)[0]

l = 0

Tm = np.zeros((N, N))
Vm = np.zeros((N, N))
Sm = np.zeros((N, N))

for al in range(N):
    for bet in range (N):
        Tm[al][bet] = T(al, bet, l)
        Vm[al][bet] = V(al, bet, l)
        Sm[al][bet] = S(al, bet, l)

print(Tm, Vm)