import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
  return np.sin(np.sqrt(x))

def romberg(f, a, b, n):
  R = np.zeros((n + 1, n + 1))

  kmax=1
  h = b-a 
  R[0][0] = (h/2.0)*(f(a)+f(b))

  for i in range(1, n+1):
    h = h/2.0; sum = 0
    kmax = kmax*2

    for k in range(1, kmax, 2):
      sum += f(a+k*h)

    R[i][0] = (0.5*R[i-1][0]) + (sum*h)

    for j in range(1, i+1):
      R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / (np.power(4.0, j) - 1.0)
  return R

print("Expected reuslt I_e={}".format(quad(f, 0, 1)))
print("Romberg integration I_r={}", romberg(f, 0, 1, 5))