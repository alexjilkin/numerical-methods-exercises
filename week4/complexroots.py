import numpy as np
LA = np.linalg

# p ---> p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]
# p starts with the ^n term
def myroots(N, p):

  # Creates the needed matrix A, adds the polynomial as the first row.
  A = np.identity(N - 1).tolist()
  ex = [-(p[i + 1] / p[0]) for i in range(0, N)]
  A.insert(0, ex)

  # Adds a column of zeros
  for i in range(1, N):
    A[i].append(0)

  print(A)
  w, v = LA.eig(A)

  return w

# The first one should have 3
polynomials = [[1, 6, 9], [5, 5, 5, 7, 8], [14, 15, 16, 17]]
for p in polynomials:
  roots = myroots(len(p) - 1, p)
  np_roots = np.roots(p)

  print ("for p={} \n myroots(p)={} \n np.roots(p)={}".format(p, roots, np_roots))

