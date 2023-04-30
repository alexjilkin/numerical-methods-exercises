import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
from scipy.optimize import least_squares

def f(x):
    return np.sin(np.pi * x)

# Primitive polynomial basis xj(xi)
def X(j, xi):
    return xi ** j

# Primitive polynomial regularized basis xj(xi)
def X_reg(j, xi):
    return (xi / 2) ** j 

# Legandere base function with mapping to [-2, 2]
def X_leg(j, xi):
    return legendre(j)((2 * (xi + 2) / 4) - 1)

# Returns a funcs which uses legandere as basis function 
# to evaluate a point with coefficients coef
def leg(x, coef):
    sum = 0

    for (i, coe) in enumerate(coef):
        sum += coe * legendre(i)(x)
    return sum
    

# Fits a polynomial with the given X(j) base function
# x: x point
# pol: a function (x, coef) that evaluates a function with coef at point x
def fit(X, pol):
    ns = [5, 10, 15, 20, 25]

    x = np.linspace(-2, 2, 200)
    # Plot target function
    plt.plot(x, f(x), linewidth=3, label="f")

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
        coef0 = np.zeros(n)

        # Solve by least squares
        res = least_squares(lambda coef: np.dot(alpha, coef) - beta, coef0, method='lm')

        # Can it be solved just by linear algebra?
        # sol = np.dot(np.linalg.inv(alpha), beta)

        x = np.linspace(-2, 2, 500)
        
        y = pol(x, res.x)
        # Calculates the error from the target function, prints and plots.
        err = np.linalg.norm(f(x) - y)
        print(f"n={n} err={err}")
        plt.plot(x, y , '--', label=f"n={n}")

    plt.ylim(-3, 3)
    plt.legend()
    plt.show()

# fit(X, lambda x, coef: np.polynomial.Polynomial(coef)(x)) # (a)
# fit(X_reg, lambda x, coef: np.polynomial.Polynomial(coef)(x / 2)) # (b)
fit(X_leg, lambda x, coef: leg(x/2, coef)) # (c)