import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Velocity of sound
v = 343

A = 1
l = 100

# Fundumental freq
f = v / (2 * l)
print(f)
w = l / 50

def flat(x):
    return np.where(np.abs(x) <= w/2, A, 0)

def round(x):
    return np.where(np.abs(x) <= w/2, A * np.sqrt(1 - (x**2)), 0)

def gaus(x):
    return   A * np.exp(-((4 * np.log(2) * x**2)/w**2))

funcs = [flat, round, gaus]

for f in funcs:
    N = 1000
    x = np.linspace(-l/2, l/2, N)
    
    yf = np.abs(fft(f(x)))

    df = 1 / N
    xf = np.abs(fftfreq(N, df))

    # plt.plot(x, [f(i) for i in x] )
    plt.plot(xf, yf, label=f.__name__)

plt.legend()
plt.show()


