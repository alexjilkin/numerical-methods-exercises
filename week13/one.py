import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from scipy.special import erf

# Function for x
def x(i):
    return (i - 1) / 10

# Returns a value for x with a Polynomial with coef of size n
# If isOdd then returns only an odd coef polynomial
def pol(x, coef):
    return np.polynomial.Polynomial(coef)(x)

# Function from (c)
def better_f(x, coef):
    p1, p2, p3, p4, p5 = coef
    z = 1 / (1 + x)

    return p1 + np.exp(-x**2) * ( p2 + (p3*z) + (p4 * z**2) + (p5 * z**3))

def odd_coef(coef):
    return np.insert(coef, np.arange(0, len(coef) - 1), 0)

# Plot the error function
lins = np.linspace(0, 1)
plt.plot(lins, erf(lins), label=f"erf", linewidth=3)

# Fits a polynomial of degree range(1, 11) for the given 11 data points.
# Plots and prints the max error of each from the intended erf()
# isOdd = True if we want to get an only odd coef polynomial.
def fit(test_f):
    for n in range(1, 11):
        xs = np.array([x(i) for i in range(1, 12)])

        # Initial coef 
        coef0 = np.zeros(n) + 1
        res = least_squares(lambda coef: test_f(xs, coef) - erf(xs), coef0, method='lm')

        if (res.success != True):
            print("Failed to fit")

        coef = res.x

        err = np.abs(erf(xs) - test_f(xs, coef))
        print(f"n={n}, max_err={err.max()}")
        plt.plot(lins, test_f(lins, coef), '--', label=f"n={n}")

    plt.legend()
    plt.show()

fit(pol)









