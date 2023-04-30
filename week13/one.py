import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from scipy.special import erf

# Function for x
def x(i):
    return (i - 1) / 10

# Returns a value for x with a Polynomial with coef of size n
def pol(x, coef):
    return np.polynomial.Polynomial(coef)(x)

# Returns a value for x with an odd degree Polynomial with coef of size 2n - 1
def pol_odd(x, coef):
    return np.polynomial.Polynomial(odd_coef(coef))(x)

# Function from (c)
def better_f(x, coef):
    p1, p2, p3, p4, p5 = coef
    z = 1 / (1 + x)

    return p1 + np.exp(-x**2) * (p2 + (p3*z) + (p4 * z**2) + (p5 * z**3))

# Creates odd coeffecients of size (2 * len(coef) - 1) by inserting 0 elements.
def odd_coef(coef):
    return np.insert(coef, np.arange(0, len(coef)), 0)

# Plot the error function
lins = np.linspace(0, 1)
plt.plot(lins, erf(lins), label=f"erf", linewidth=3)

# Fits a polynomial of degree 1 to 10 for the given 11 data points.
# Plots and prints the max error of each from the target erf()
def fit(f):
    for n in range(2, 12):
        xs = np.array([x(i) for i in range(1, 12)])

        # Initial coef 
        coef0 = np.zeros(n) + 1

        # Fit paramters of f to act as an erf
        res = least_squares(lambda coef: f(xs, coef) - erf(xs), coef0, method='lm')
        if (res.success != True):
            print("Failed to fit")

        coef = res.x

        err = np.abs(erf(xs) - f(xs, coef))
        print(f"n={n}, max_err={err.max():.5}, cost={res.cost:.5}")
        plt.plot(lins, f(lins, coef), '--', label=f"n={n}")

    plt.legend()
    plt.show()

# Fits the function from (c)
def fit_better():
    xs = np.array([x(i) for i in range(1, 12)])

    # Initial coef 
    coef0 = np.zeros(5) + 1

    # Fit paramters of better_f to act as an erf
    res = least_squares(lambda coef: better_f(xs, coef) - erf(xs), coef0, method='lm')

    if (res.success != True):
        print("Failed to fit")

    coef = res.x

    err = np.abs(erf(xs) - better_f(xs, coef))
    print(f"max_err={err.max():.5}, cost={res.cost:.5}")
    plt.plot(lins, better_f(lins, coef), '--', label=f"fitting")

    plt.legend()
    plt.show()

# fit(pol)
fit_better()









