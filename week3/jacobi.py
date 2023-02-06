import numpy as np
from numpy import linalg as LA
import random
import math

# Returns an array of eigenvalues of an N*N matrix Q
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

# Testing jacobi against linalg with 3 predefined matrices, and one random
def test_jacobi():
  mat1 = np.array([[1, 2, 3], [2, 3, -10], [3, -10, 3]])
  mat2 = np.array([[1, 5, 200, 100], [5, 2, 0, 0], [200, 0, 3, 0], [100, 0, 0, 5]])
  mat3 = np.array([[1, 0, 0, 100], [0, 2, 0, 0], [0, 0, 3, 10], [100, 0, 10, 5]])
  mat4 = get_symm_matrix(10)

  matrices = [mat1, mat2, mat3, mat4]

  for matrix in matrices:
    jacobi_values = jacobi(matrix, len(matrix))
    linalg_values, v =  LA.eig(matrix)

    print("For the matrix \n {} \n the jacobi eigenvalues are: {} \n while the result from numpy's linalg is: {}".format(matrix, jacobi_values, linalg_values))


# Generates random symmetric matrix of size N
def get_symm_matrix(N):
  b = np.random.randint(-100, 100 + 1, size=(N,N))
  return (b + b.T)/2

# Calculates the error propagtion of the jacobi algorithem for a N x N random symmetric matrix, and a randomply placed dq inside
def err_propag(N,dq):
  A = get_symm_matrix(N)
  lambdas = jacobi(A, len(A))

  rand_i = int(random.random() * N)
  rand_j = int(random.random() * N)

  P = A.copy()
  P[rand_i, rand_j] += dq 
  p_lambdas = jacobi(P, len(P))

  d_lambdas = p_lambdas - lambdas

  # default norm is 2
  f = LA.norm(d_lambdas) / (LA.norm(lambdas) * dq)
  return f

# Calculates the mean and std of 100 error propogations for N x N random matrix and dq pertubation
def err_propag_stats(N, dq): 
  stats = np.array([err_propag(N, dq) for i in range(0, 100)])

  print("For N={}, dq={} \n The error propag mean: {}, standard deviation: {} \n".format(N, dq, stats.mean(), stats.std()))

# err_propag_stats(20, 1)
# err_propag_stats(12, 0.1)
# err_propag_stats(10, 0.001)
err_propag_stats(30, 20)

#test_jacobi()
# print(err_propag(10, 1))