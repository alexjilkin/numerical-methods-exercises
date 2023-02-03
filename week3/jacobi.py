import numpy as np
from numpy import linalg as LA
import random
import math

# Returns an array of eigenvalues of a N*N matrix Q
def jacobi(Q, N):
  A_arr = [Q.copy()]
  iterations = 30

  for i in range(0, iterations):
    B = A_arr[i]

    for p in range(0, N - 1):
      for q in range(p + 1, N):
        C = 1
        if (B[p][q] != 0):
          C = (B[p][p] - B[q][q]) / math.sqrt((B[p][p] - B[q][q])**2 + (4 * B[p][q] ** 2))

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

def test_jacobi():
  mat3 = np.array([[1, 2, 3], [2, 3, -10], [3, -10, 3]])
  mat4 = np.array([[1, 5, 200, 100], [5, 2, 0, 0], [200, 0, 3, 0], [100, 0, 0, 5]])
  mat4_1 = np.array([[1, 0, 0, 100], [0, 2, 0, 0], [0, 0, 3, 10], [100, 0, 10, 5]])
  mat = get_symm_matrix(10)
  print(jacobi(mat, len(mat)))

  # print eigen values from numpy's linalg
  w, v = LA.eig(mat)
  print(w)


# Generates random symmetric matrix of size N
def get_symm_matrix(N):
  b = np.random.random_integers(-100,100,size=(N,N))
  return (b + b.T)/2

test_jacobi()

# print(get_symm_matrix(10))
def err_propag(N,dq):
  A = get_symm_matrix(N)
  lambdas = jacobi(A, len(A))

  rand_i = int(random.random() * N)
  rand_j = int(random.random() * N)

  P = A.copy()
  P[rand_i, rand_j] += dq 
  p_lambdas = jacobi(P, len(P))

  d_lambdas = lambdas - p_lambdas

  print(d_lambdas)
  f = LA.norm(d_lambdas) / (LA.norm(lambdas) * dq)
  print(f)


# err_propag(10, 1)