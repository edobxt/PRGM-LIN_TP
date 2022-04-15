import numpy as np

def maximal(A):
  return np.argmax(A[A.shape[0] - 1]) # retourne l'index de la valeur max 