import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

def f(x):
    return np.sin(np.pi * x)

def X(j, xi):
    return xi ** j

def X_reg(j, xi):
    return (xi / 2) ** j

def X_leg(j, xi):
    return legendre(j)((2 * xi) / 4)

def fit(X):
    ns = [5, 10, 15, 20, 25]

    for n in ns:
        x = np.linspace(-2, 2, n)
    
        # Builds A matrix
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i][j] = X(j, x[i])

        # Calculates alpha and beta from lecture notes
        b = f(x)
        alpha = np.dot(A.T, A)
        beta = np.dot(A.T, b)

        # Solves linear equations and builds polynomial
        sol = np.linalg.solve(alpha, beta)
        pol = np.polynomial.Polynomial(sol)

        x = np.linspace(-2, 2, 200)
        
        err = np.linalg.norm(f(x) - pol(x))
        print(f"n={n} err={err}")
        plt.plot(x, pol(x), label=f"n={n}")

    x = np.linspace(-2, 2, 200)
    plt.plot(x, f(x), label="f")
    plt.ylim(-3, 3)
    plt.legend()
    plt.show()

fit(X)