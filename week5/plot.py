import matplotlib.pyplot as plt
import numpy as np


# This one is not correct
def f1(x):
  return (11/60)*x**2 - (51/60) *x + 1

def f2(x):
  return (1/10)*x**2 - (6/10)*x + 1

# This one is not correct
plt.plot(np.linspace(-0.5, 3.5, 100), f1(np.linspace(-0.5, 3.5, 100)))


plt.plot(np.linspace(-0.5, 3.5, 100), f2(np.linspace(-0.5, 3.5, 100)))

plt.show()