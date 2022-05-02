import numpy as np

def index_du_un_de_colonne(A, colonne):
  l, m = np.shape(A)
  
  for i in np.arange(l):
    if A[i][colonne] == 1:
      return i

def point(A):
  l, m = np.shape(A)

  B = []
  for i in np.arange(m):
    if i < m-1:
      if A[l-1, i] == 0:
        index_ligne_du_un = index_du_un_de_colonne(A, i)
        B.insert(i, A[index_ligne_du_un, m-1])
      else:
        B.insert(i, 0)
    
  return B