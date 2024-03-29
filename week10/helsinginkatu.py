import random
import matplotlib.pyplot as plt
import numpy as np

from collections import Counter

d1 = 512
d2 = 252
db = 2048
dl = 512

p_step = 0.01

def flip(p):
    return True if random.random() < p else False

def is_at_pena(x, n):
  return x == d2 and flip(1 - 2**(-n/d2)) and flip(2**(-n/dl))

def is_at_home(x, n):
  # Doesn't miss home with prob 0.9
  return x == -d1 and flip(0.9)

def is_at_bar(x, n):
  return x == 0 and flip(1 - 2**(-n/db))

def is_at_tank(x, n):
  return x == -1154

def is_at_kurvi(x, n):
  return x == 1154

# Returns a tuple of (end place, number of steps)
# with endplace can be one of Pena, Home, Bar, Tank
def simulate():
  end = False
  x = 0
  n = 0
  direction = 1

  while not end:
    if (flip(p_step)):
      direction = direction * -1
    
    x += direction
    n += 1

    if is_at_kurvi(x, n):
      x -= 1
    elif (is_at_pena(x, n)):
      return ("Pena", n)
    elif (is_at_home(x, n)):
      return ("Home", n)
    elif (is_at_bar(x, n)):
      return ("Bar", n)
    elif (is_at_tank(x, n)):
      return ("Tank", n)

simulations = [simulate() for _ in range(365)]
print(Counter([place for place, n in simulations]))

max_step = np.max([n for _, n in simulations]) + 1

places = ["Pena", "Home", "Bar", "Tank"]
samples = {}

for place in places:
  samples[place] = np.zeros(max_step)

# Transform to an array based on stems
for place, n in simulations:
  samples[place][n] += 1

for place in places:
  plt.scatter(np.arange(max_step), np.cumsum(samples[place]), s=1, label=place)

plt.legend()
plt.show()
