import numpy as np
from numpy import linalg as LA

import math

def jacobi(Q, N):
  A_arr = [Q.copy()]

  for i in range(0, 10):
    B = A_arr[i]
    for p in range(0, N - 1):
      for q in range(p + 1, N):
        C = (Q[p][p] - Q[q][q]) / math.sqrt(math.pow(Q[p][p] - Q[q][q], 2) + (4 * Q[p][q] * Q[p][q]))
        c = np.sqrt((1 + C) / 2)
        s = np.sign(Q[p][q]) * np.sqrt((1 - C) / 2)

        Q_pq = np.identity(N);
        
        Q_pq[p][p] = c
        Q_pq[q][q] = c
        Q_pq[p][q] = -s
        Q_pq[q][p] = s
        
        B = np.matmul(np.matmul(np.transpose(Q_pq), B), Q_pq)

    A_arr.append(B)
  print(A_arr)

mat = np.array([[5, 1, 4], [1, 2, 1], [4, 1, 6]])
print(mat)

jacobi(mat, len(mat))

print(LA.eig(mat))
  
  