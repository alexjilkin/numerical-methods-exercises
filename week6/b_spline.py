import numpy as np
import matplotlib.pyplot as plt

# Normalized by 1/2
def f1(t):
  if (t >= 0 and t < 1):
    return t 
  elif (t >= 1 and t < 2):
    return (2 - t)
  else:
    return 0
  
def f2(t):
  if (t >= 0 and t < 1):
    return (t**2 / 2)
  elif (t >= 1 and t < 2):
    return (-(t**2) + (6*t) - 3) / 2
  elif (t >= 2 and t < 3):
    return (((3 - t)**2) / 2)
  else:
    return 0
  
linspace = np.linspace(0, 5, 100)

plt.plot(linspace, [f1(x) for x in linspace], label="k=1")
plt.plot(linspace, [f2(x) for x in linspace], label="k=2")
plt.legend()
plt.show()