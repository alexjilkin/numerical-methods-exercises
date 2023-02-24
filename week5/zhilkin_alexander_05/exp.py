import numpy as np

def myexp(x):
  res = (np.exp(x) + 0.5)/(0.5 - np.exp(x)) 
  return res 
