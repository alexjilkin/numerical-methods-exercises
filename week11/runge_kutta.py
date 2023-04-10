import numpy as np
import matplotlib.pyplot as plt

# To solve y'' + y = 0 we substitue u = y' and get u' = -y
def g(t, y, u):
    return -y
def f(t, y, u):
    return u

# Evaluates the result the DE y'' + y = 0 using RK4
# in the [a, b] range with y0 and y'0 as initial values
def runge_kutta_solver(a, b, N, y0, yp0):
  h = (b - a) / N

  t = np.linspace(a, b, N+1)
  y = np.zeros(N+1)
  u = np.zeros(N+1)

  y[0] = y0
  u[0] = yp0
  
  for i in range(N):
    k1 = h * f(t[i], y[i], u[i])
    l1 = h * g(t[i], y[i], u[i])
    k2 = h * f(t[i] + h/2, y[i] + k1/2, u[i] + l1/2)
    l2 = h * g(t[i] + h/2, y[i] + k1/2, u[i] + l1/2)
    k3 = h * f(t[i] + h/2, y[i] + k2/2, u[i] + l2/2)
    l3 = h * g(t[i] + h/2, y[i] + k2/2, u[i] + l2/2)
    k4 = h * f(t[i] + h, y[i] + k3, u[i] + l3)
    l4 = h * g(t[i] + h, y[i] + k3, u[i] + l3)
    y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    u[i+1] = u[i] + (l1 + 2*l2 + 2*l3 + l4)  /6

  return t, y

def plot():
    t, y = runge_kutta_solver(0, 10, 100, 1, 0)
    print(t, y)
    plt.plot(t, y, ":", label="RK4")
    x = np.linspace(0, 10)
    plt.plot(x, np.cos(x), alpha=0.5, label="analytical cos(x)")
    plt.legend()
    plt.show()


plot()