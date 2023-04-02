import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Just P(x) from question 3 for testing.
def f(x):
    return (x**3) * np.exp(-0.5*x**2) / np.sqrt(2 * np.pi)
    
mu = 3.7
sigma_sq = 76.6
sigma = 8.75214259482

points = np.array([21.9514, 28.1882, 28.7511, 31.1946, 37.3700, 20.5656, 31.2570, 31.6869, 37.4599, 26.0999,
29.9478, 36.6224, 34.1511, 25.8640, 33.2204, 29.4145, 24.8233, 23.7741, 25.2026, 26.4967])

x = np.linspace(-10, 10, 1000)
y = norm.pdf(x, loc = mu, scale=sigma)

plt.plot(x, y)
plt.scatter(points, norm.pdf(points, loc = mu, scale=sigma), s=10, c='r')
plt.show()
