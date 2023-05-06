import numpy as np
from scipy.integrate import quad

alpha_0 = 0.01
beta = 2

def alpha(i):
    return alpha_0 * (beta ** (i))

def N(al, bet):
    if (al == bet):
        return 1
    
    return 0
    # return 1 / (quad(lambda r: r ** 2 * np.exp(-al * r**2 ), 0, np.inf)[0])
    # return ((2 * al) / np.pi) ** 0.75

def R(al, r):
    return N * (r ** l) * np.exp(-al * (r ** 2))

def T(al, bet, l):
    def T_int1(r):
        return (r**(2*l)) * np.exp((r**2) * (-al - bet)) * (l - 2*al*r*r) * (l - 2*bet*r*r)
    def T_int2(r):
        return (r ** (2*l)) * np.exp((r**2) * (-al - bet))

    return 0.5 * N(al, bet) * (quad(T_int1, 0, np.inf)[0] + (l * (l+1) * quad(T_int2, 0, np.inf)[0]))

def V(al, bet, l):
    def V_int(r):
        return -(r ** (2*l +1)) * np.exp(r * r * (-al - bet)) 
    
    return N(al, bet) * quad(V_int, 0, np.inf)[0]

def S(al, bet, l):
    return N(al, bet) * quad(lambda r: (r ** (2*l + 2)) * np.exp(r * r * (-al - bet)), 0, np.inf)[0]

l = 2
Num = 25

Tm = np.zeros((Num, Num))
Vm = np.zeros((Num, Num))
Sm = np.zeros((Num, Num))

for al in range(Num):
    for bet in range (Num):
        Tm[al][bet] = T(alpha(al), alpha(bet), l)
        Vm[al][bet] = V(alpha(al), alpha(bet), l)
        Sm[al][bet] = S(alpha(al), alpha(bet), l)

H = Tm + Vm

Lambda, U = np.linalg.eig(Sm)
Eps = np.diag(Lambda ** -0.5)

U_inv = np.linalg.inv(U)

# S^(-1/2)
X = U @ Eps @ U_inv

X_t = np.transpose(X)
H_tilda = X_t @ H @ X

E, Ctild = np.linalg.eig(H_tilda)
print(E)


