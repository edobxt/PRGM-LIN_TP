import numpy as np
'''
EXO 2 : Étant donné :
	- une ligne pivot p
	- une colonne pivot q
	- un dictionnaire A
Donner un script pivot(A, p, q) qui prend un tableau Â 
de même dimension que A et qui donne un nouveau dictionnaire du simplexe 
'''

def pivot(A, p, q):
  # copie de la matrice dans une autre variable
  N = A.copy()

  # recupere les dimensions de la matrice
  l, m = np.shape(N)

  # pivotement a base de calculs vectoriels
  for k in np.arange(l):
    if k == p:
      N[k, :] = A[k, :]/A[k, q]
    else:
      N[k, :] = A[k, :] - A[k, q]/A[p, q]*A[p, :]

  return N
