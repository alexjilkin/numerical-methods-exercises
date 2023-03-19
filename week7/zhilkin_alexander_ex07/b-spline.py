import numpy as np
import matplotlib.pyplot as plt

# N3_i b-splines 
def N3_i(t, i, x):
  y = 0
  if t >= x[i] and t < x[i+1]:
    y = (t-i) / (3) * (t-i) * (t-i)/2
  elif t >= x[i+1] and t < x[i+2]:
    y = ((t-i)/3)*((t-i)/2*(i+2-t)+((i+3-t)/2)*(t-(i+1)))+(i+3+1-t)/3*(t-(i+1))/2*(t-(i+1))
  elif t >= x[i+2] and t <= x[i+3]:
    y= (t-i)/3*(i+3-t)/2*(i+3-t)+ (i+4-t)/3 * ((t-(i+1))/2*(i+3-t) + (i+4-t)/2*(t-(i+2)) )
  elif t >= x[i+3] and t <= x[i+4]:
    y = (i+4-t)/3*(i+4-t)/2*(i+4-t)
  else:
    y = 0

  return y

# Our domain
a = 0
b = 10

# y values fo the control points
y_i = [-2, 2, 4, 5, 1, 5, 1, 5 , 6, 8]
n = len(y_i)
# evenly spaced t_i control points.
x_i = [a + (i * (b - a)) / n for i in range(n + 3)]

# Interpolated function value at t
def y(t):
  return np.sum([y_i[i] * N3_i(t, y_i[i], x_i) for i in range(len(y_i))])

plt.plot(np.linspace(a, b , 100), [y(t) for t in np.linspace(a, b, 100)])
plt.show()