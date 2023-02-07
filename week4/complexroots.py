import numpy as np

import math

LA = np.linalg

def myroots(N, p):
  A = np.identity(N)
  print(p)
  for i in range(0, N):
    A[0][i] = -(p[i + 1] / p[0])

  print(A)

  w, v = LA.eig(A)

  print(w)
  
myroots(2, [1, 6, 9])