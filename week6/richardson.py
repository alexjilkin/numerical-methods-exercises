import numpy as np



def f(x):
  return np.sin(np.exp(-(x**2)))



def richardson_derivative(x):
  N = 5
  h = 0.1
  D = np.zeros([N + 1, N + 1])
  hh=h;

  for i in range(N + 1):
    D[i][0]=(f(x+hh)-f(x-hh))/(2.0*hh)

    for j in range(i):
      D[i][j+1] = D[i][j]+(D[i][j]-D[i-1][j])/(pow(4.0,j+1.0)-1.0)
    hh = hh/2.0
  
  return D[N, N]


x = 1
richardson_res = richardson_derivative(x)
print("Richardson extrapolation N=5, h=0.1 for f(x): {}".format(richardson_res))
steps = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
for h in steps:
  approx_derivative = (f(x + h) - f(x)) / h
  print("h={}, error={}".format(h, np.abs(richardson_res - approx_derivative)))