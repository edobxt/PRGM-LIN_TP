import numpy as np

def critere_maximalite(A):
  # recuperer la derniere ligne
  derniere_ligne = A[A.shape[0] - 1]
  
  # retourne l'index de la valeur max de la derniere ligne
  return np.argmax(derniere_ligne)