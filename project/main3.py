import numpy as np
from scipy.integrate import quad

alpha_0 = 10 ** -2
beta = 2

def alpha(i):
    return alpha_0 * (beta ** (i - 1))

def N(al):
    return 1 / (quad(lambda r: r ** (2 * l) * np.exp(-al * r**2 ), 0, np.inf)[0])

def V(r):
    return -(1/r)

def R(al, r):
    return N * (r ** l) * np.exp(-al * (r ** 2))

def T(al, bet, l):
    def T_int1(r):
        return (r ** 2) * (r ** (2 * l - 1)) * np.exp(r * r * (-al - bet)) * (l - 2*al*r) * (l - 2*bet*r)
    def T_int2(r):
        return (r ** (2 * l)) * np.exp(r * r * (-al - bet))

    return 0.5 * (N(al) * N(beta) * quad(T_int1, 0, np.inf)[0] + l * (l+1) * quad(T_int2, 0, np.inf)[0])

def V(al, bet, l):
    def V_int(r):
        return np.exp(r * r * (-al - bet)) * (r ** (2*l +1))
    
    return -N(al) * N(bet) * quad(V_int, 0, np.inf)[0]

def S(al, bet, l):
    return N(al) * N(bet) * quad(lambda r: r ** (2 * l + 2) * np.exp(r * r * (-al - bet)), 0, np.inf)[0]

l = 0

Num = 25

Tm = np.zeros((Num, Num))
Vm = np.zeros((Num, Num))
Sm = np.zeros((Num, Num))


for al in range(Num):
    for bet in range (Num):
        Tm[al][bet] = T(alpha(al), bet, l)
        Vm[al][bet] = V(alpha(al), bet, l)
        Sm[al][bet] = S(alpha(al), bet, l)

H = Tm + Vm

Lambda, U = np.linalg.eig(Sm)
Eps = np.diag(np.sqrt(Lambda))
Eps_inv = np.linalg.inv(Eps)

U_inv = np.linalg.inv(U)

# S^(-1/2)
X = U @ Eps_inv @ U_inv

X_t = np.transpose(X)
H_tilda = X_t @ H @ X

E, Ctild = np.linalg.eig(H_tilda)
print(E)


