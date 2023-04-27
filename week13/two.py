import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(np.pi * x)

def X(j, xi):
    return xi ** j


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
    alpha = np.matmul(A.T, A)
    beta = np.matmul(A.T, b)

    # Solves linear equations and builds polynomial
    sol = np.linalg.solve(alpha, beta)
    pol = np.polynomial.Polynomial(sol)

    x = np.linspace(-2, 2, 200)
    
    err = np.linalg.norm(f(x) - pol(x))
    print(f"n={n} err={err}")
    plt.plot(x, pol(x), label=f"n={n}")

x = np.linspace(-2, 2, 200)
plt.plot(x, f(x), label="f")
plt.legend()
plt.show()
