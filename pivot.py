import numpy as np
'''
EXO 2 : Étant donné :
	- une ligne pivot p
	- une colonne pivot q
	- un dictionnaire A
Donner un script pivot(A, p, q) qui donne en entre un tableau 

Â de même dimension que A et qui donne un nouveau dictionnaire du simplexe 
'''

def pivot(A, p, q):
  N = A.copy()
  l, m = np.shape(N)

  for k in np.arange(l):
    if k == p:
      N[k, :] = A[k, :]/A[k, q]
    else:
      N[k, :] = A[k, :] - A[k, q]/A[p, q]*A[p, :]

  return N