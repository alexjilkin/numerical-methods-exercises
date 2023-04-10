import numpy as np
import matplotlib.pyplot as plt
from runge_kutta import runge_kutta_solver
from scipy import optimize

def y_analy(x):
    return np.cos(x) + (0.5460 * np.sin(x))

def shooting_solver(a,b,N,y0,y1):
    # Define a new function dependant on the angle k
    def f(k):
        t, y = runge_kutta_solver(a, b, N, y0, k)
        return y[-1] - y1
    
    # Find the root on the new function, which is the needed k
    sol = optimize.root(f, 5, method='hybr')

    if (not sol.success):
        raise Exception('Could not find root')
    k = sol.x

    return runge_kutta_solver(a, b, N, y0, k)

t, y = shooting_solver(0, 1, 30, 1, 1)

plt.plot(t, y, '--' ,label="shooting")

x = np.linspace(0, 1)
plt.plot(x, y_analy(x), label="analytical y(x)", alpha=0.5)
plt.legend()
plt.show()
