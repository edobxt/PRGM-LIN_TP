import numpy as np
from point import point

def point_simplifie(A, p):
  l, m = np.shape(A)
  derniere_ligne = A[A.shape[0] - 1]
  p_s = []
  
  for i in np.arange(m):
    if derniere_ligne[i] > 0:
      p_s.insert(i, p[i])
    
  return p_s