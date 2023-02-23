import numpy as np

N = 6
h = 0.1

def f(x):
    return np.sin(np.exp(-(x**2)))

D = np.zeros([N + 1, N + 1])
x = 3

def derivative():
    hh=h;

    for i in range(N + 1):
        D[i][0]=(f(x+hh)-f(x-hh))/(2.0*hh)
    
        for j in range(i):
            D[i][j+1] = D[i][j]+(D[i][j]-D[i-1][j])/(pow(4.0,j+1.0)-1.0);
        hh = hh/2.0;
 
derivative()
h = 1e-5

print ((f(x + h) - f(x)) / h)
print(D)