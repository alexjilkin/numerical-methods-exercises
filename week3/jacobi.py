import numpy as np
from numpy import linalg as LA

import math

def jacobi(Q, N):
  A_arr = [Q.copy()]
  iterations = 30

  for i in range(0, iterations):
    B = A_arr[i]

    for p in range(0, N - 1):
      for q in range(p + 1, N):
        C = (B[p][p] - B[q][q]) / math.sqrt(math.pow(B[p][p] - B[q][q], 2) + (4 * B[p][q] * B[p][q]))
        c = np.sqrt((1 + C) / 2)
        s = np.sign(B[p][q]) * np.sqrt((1 - C) / 2)

        Q_pq = np.identity(N);
        
        Q_pq[p][p] = c
        Q_pq[q][q] = c
        Q_pq[p][q] = -s
        Q_pq[q][p] = s
        
        B = np.matmul(np.matmul(np.transpose(Q_pq), B), Q_pq)

    A_arr.append(B)
  return np.diagonal(A_arr[iterations])

mat = np.array([[1, 2, 3], [2, 3, -10], [3, -10, 3]])
print(mat)

print(jacobi(mat, len(mat)))

w, v = LA.eig(mat)

print(w)
  
  