import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from scipy.special import erf

# Function for x
def x(i):
    return (i - 1) / 10

# Returns a value for x with a Polynomial with coef of size n
def pol(x, coef):
    return np.polynomial.Polynomial(coef)(np.array(x))

# Plot the error function
lins = np.linspace(0, 1)
plt.plot(lins, erf(lins), label=f"erf", linewidth=3)

for n in range(1, 11):
    xs = [x(i) for i in range(1, 12)]

    def obj_func(coef):
        return pol(xs, coef) - erf(xs)

    args0 = np.zeros(n) + 1

    res = least_squares(obj_func, args0, method='lm')

    if (res.success != True):
        print("Failed to fit")

    

    plt.plot(lins, np.polynomial.Polynomial(res.x)(lins), '--', label=f"n={n}")

plt.legend()
plt.show()
print(res)








