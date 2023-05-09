import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def alpha(alpha_0, beta, i):
    return alpha_0 * (beta ** (i))

def V_p(r):
    return -(1 / r)

def Nl(al, bet, l):
    if (al == bet):
        return 1 / quad(lambda r: r**2 * (r ** (2*l)) * np.exp(-2*al*r**2), 0, np.inf)[0]
    return 0

def R(r, al, l):
    return (r ** l) * np.exp(-al * (r ** 2))

def T(al, bet, l):
    def T_int1(r):
        return (r**2) * np.exp(-r**2 * (al + bet)) * (l*(r**(l-1)) - 2*al*(r**(l+1))) * (l*(r**(l-1)) - 2*bet*(r**(l+1)))
    def T_int2(r):
        return (r ** (2*l)) * np.exp(-r**2 * (al + bet))

    return 0.5 * Nl(al, bet, l) * (quad(T_int1, 0, np.inf)[0] + (l * (l+1) * quad(T_int2, 0, np.inf)[0]))

def V(al, bet, l):
    def V_int(r):
        return (r ** (2*l + 2)) * np.exp(-r**2 * (al + bet)) * V_p(r)
    
    return Nl(al, bet, l)  * quad(V_int, 0, np.inf)[0]

def S(al, bet, l):
    return Nl(al, bet, l)  * quad(lambda r: (r ** (2*l + 2)) * np.exp(-r**2 * (al+bet)), 0, np.inf)[0]

def comp(N, alpha0, beta, l):
    Tm = np.zeros((N, N))
    Vm = np.zeros((N, N))
    Sm = np.zeros((N, N))

    for al in range(N):
        for bet in range (N):
            al_i = alpha(alpha0, beta, al)
            bet_i = alpha(alpha0, beta, bet)

            Tm[al][bet] = T(al_i, bet_i, l)
            Vm[al][bet] = V(al_i, bet_i, l)
            Sm[al][bet] = S(al_i, bet_i, l)

    H = Tm + Vm

    Lambda, U = np.linalg.eig(Sm)
    Eps = np.diag(Lambda ** -0.5)

    # S^(-1/2)
    X = U @ Eps @ np.linalg.inv(U)

    X_t = np.transpose(X)
    H_tilda = X_t @ H @ X

    E, Ctild = np.linalg.eig(H_tilda)
    C = X * Ctild
    
    return E, C

N = 25
l = 0

E, C = comp(N, 0.01, 2, l)

print(E)
def R_(r, C):

    sum = 0
    for i in range(N):
        al = alpha(0.01, 2, i)
        sum += C[i][1] * (r ** l) * np.exp(-al * r**2)

    return sum

def R(r):
    return 2 * np.exp(-r)

r = np.linspace(0, 2 * np.pi)

plt.plot(r, R(r))
plt.plot(r, R_(r, C))
plt.show()

