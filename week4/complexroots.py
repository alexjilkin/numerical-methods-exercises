import numpy as np

import math

LA = np.linalg

def myroots(N, p):
  A = np.identity(N)
  print(p)
  for i in range(0, N):
    A[0][i] = -(p[N - 1 - i] / p[N - i])

  print(A)

  w, v = LA.eig(A)

  print(w)
  
myroots(3, [1, 2, 3, 3])