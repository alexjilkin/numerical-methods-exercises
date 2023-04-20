import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

with open('./samples/sample1.dat') as f:
    lines = f.readlines()

samples = np.array([list(map(lambda n: float(n), line.strip().split())) for line in lines])
samples = samples[1:]

N = len(samples)

# Arange samples around the 0 point
samples[:, 1] = (samples[:, 1] - 2.5) 

yf = np.abs(fft(samples[:, 1]))

df = samples[1][0] - samples[2][0]
xf =  np.abs(fftfreq(N, df))

plt.plot(xf, yf)
plt.show()

M = int(N / 20)
window = np.hanning(M)

windowed_samples = samples[10 * M: 11 * M] * window
# windowed_samples[:, 1] = windowed_samples[:, 1] * window
yf = np.abs(fft(windowed_samples[:, 1]))
xf =  np.abs(fftfreq(M, df))
plt.plot(xf, yf)
plt.show()

# plt.xlim([0, 4000])
plt.show()