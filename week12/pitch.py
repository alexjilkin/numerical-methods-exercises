import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import stft
import matplotlib.pyplot as plt

with open('./samples/sample1.dat') as f:
    lines = f.readlines()

samples = np.array([list(map(lambda n: float(n), line.strip().split())) for line in lines])
samples = samples[1:]

N = len(samples)

# Arrange samples around the 0 point
samples[:, 1] = (samples[:, 1] - 2.5) 

yf = np.abs(fft(samples[:, 1]))

df = np.abs(samples[1][0] - samples[2][0])
xf =  np.abs(fftfreq(N, df))

# plt.plot(xf, yf)
# plt.show()

plt.specgram(samples[:, 1], Fs=(1 / df))
plt.show()

# M = int(N / 100)
# window = np.hanning(M)
# z = []
# xf =  np.abs(fftfreq(M, df))

# fft_data = np.array([])

# for i in range(100):
#     windowed_samples = samples[i * M: (i + 1) * M]
#     windowed_samples[:, 1] = windowed_samples[:, 1] * window

#     yf = np.abs(fft(windowed_samples[:, 1]))
    
#     fft_data = np.concatenate((fft_data, yf))

# fig = plt.figure(figsize = (12, 12))
 
# ax = fig.add_subplot(111, projection='3d')
# ax.pcolor(np.tile(xf, (100, 1)).flatten(), np.repeat([i for i in range(len(xf))], 100), fft_data, s=1, alpha=1)

# ax.set_xlabel("Freq")
# ax.set_ylabel("Time")
# ax.set_zlabel("Amount")

# ax.view_init(10, 90, 0)

# plt.xlim([0, 4000])
# plt.show()