import numpy as np

import math

LA = np.linalg

def myroots(N, p):
  # TODO: should be not identity
  A = np.identity(N - 1).tolist()
  ex = [-(p[i + 1] / p[0]) for i in range(0, N)]

  A.insert(0, ex)
  for i in range(1, N):
    A[i].append(0)

  print(A)
  w, v = LA.eig(A)

  print(w)
  
myroots(2, [1, 6, 9])