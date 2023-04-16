import numpy as np
import matplotlib.pyplot as plt
from runge_kutta import runge_kutta_solver
from scipy import optimize

# Analytical solution to y
def y_analy(x):
    return np.cos(x) + (0.5460 * np.sin(x))

# Solves y''+y=0 using the shooting method for y0 y1 boundary conditions
def shooting_solver(a,b,N,y0,y1):
    # Define a new function dependant on the angle k
    def f(k):
        t, y = runge_kutta_solver(a, b, N, y0, k)
        return y[-1] - y1
    
    # Find the root on the new function, which is the needed k
    sol = optimize.root(f, 1, method='hybr')

    if (not sol.success):
        raise Exception('Could not find root')
    k = sol.x
    
    # Return the numerical approximation of y with the optimal k
    return runge_kutta_solver(a, b, N, y0, k)

# Plots the solution of the equation with shooting_solver for N=[10, 30, 100]
def plot():
    Ns = [10, 30, 100]
    for N in Ns:
        t, y = shooting_solver(0, 1, N, 1, 1)

        plt.plot(t, y, '--' ,label="Shooting N={}".format(N))

    x = np.linspace(0, 1)
    plt.plot(x, y_analy(x), label="Analytical y(x)", alpha=0.5)
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

plot()