import numpy as np
'''
EXO 1 : Écrire un algo qui :
  Prend en entrée :
    - un dictionnaire du simplexe
    - un indice de colonne
  Calcul :
    - le ratio minimum
  Retourne :
    - l'indice de la ligne
'''

def ratio(A, q):
  l, m = np.shape(A)
  X = []

  for i in range(0, l-1):
    b = A[i][q]
    element = A[i][m-1]

    if b > 0:
      X.insert(i, element / b)
    else:
      X.insert(i, 10^6)

  return np.argmin(X) - 1