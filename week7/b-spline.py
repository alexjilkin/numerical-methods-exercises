import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def N3_i(t, i):
  y = 0
  if t >= i and t < i+1:
    y = (t-i) / (3) * (t-i) * (t-i)/2
  elif t >= i+1 and t < i+2:
    y = ((t-i)/3)*((t-i)/2*(i+2-t)+((i+3-t)/2)*(t-(i+1)))+(i+3+1-t)/3*(t-(i+1))/2*(t-(i+1))
  elif t >= i+2 and t <= i+3:
   y= (t-i)/3*(i+3-t)/2*(i+3-t)+ (i+4-t)/3 * ((t-(i+1))/2*(i+3-t) + (i+4-t)/2*(t-(i+2)) )
  elif t >= i+3 and t <= i+4:
    y=(i+4-t)/3*(i+4-t)/2*(i+4-t)

  return y

x_i = [0, 1, 2, 3, 4, 5, 6]
y_i = [-2, 2, 4, 5, 1, 5, 1]

def y(t):
  return np.sum([y_i[i] * N3_i(t, y_i[i]) for i in range(len(y_i))])

plt.plot(np.linspace(0, 10, 100), [y(t) for t in np.linspace(0, 10, 100)])

plt.show()