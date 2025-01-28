import numpy as np

def monte_carlo(n): # n is number of samples wanted
  x = np.random.rand(n)
  y = np.random.rand(n)

  return (x,y)
