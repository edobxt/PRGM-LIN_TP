from maximal import maximal
from pivot import pivot
from ratio import ratio

def simplexe(A):
  # copie du simplexe afin d'effectuer les opérations
  X = A.copy()

  # tant qu'il y a des positifs sur la dernière ligne
  while X[X.shape[0]-1, maximal(X)] > 0:
    # récupération de [ligne, colonne] pivot
    index_colonne_pivot = maximal(X)
    index_ligne_pivot = ratio(X, index_colonne_pivot)
    
    # pivotement
    X = pivot(X, index_ligne_pivot, index_colonne_pivot)
    
    print(f'{X} \n')
  return X