from maximal import critere_maximalite
from pivot import pivot
from ratio import ratio
from point import point
from point_simplifie import point_simplifie
import numpy as np

def simplexe(A):
  # copie du simplexe afin d'effectuer les opérations
  X = A.copy()
  l, m = np.shape(A)
  nb_pivotement = 1

  # tant qu'il y a des positifs sur la dernière ligne
  while X[X.shape[0]-1, critere_maximalite(X)] > 0:
    # récupération de la ligne et de la colonne pivot
    index_colonne_pivot = critere_maximalite(X)
    index_ligne_pivot = ratio(X, index_colonne_pivot)

    print(f'Pivotement {nb_pivotement} ⬆️')
    print(f'''
          Colonne pivot : {index_colonne_pivot + 1} \t
          Ligne pivot : {index_ligne_pivot + 1}
    ''')
    print('On obtient ⬇️')
    
    # pivotement
    X = pivot(X, index_ligne_pivot, index_colonne_pivot)
    nb_pivotement += 1
    
    print(f'{X} \n')
    
  print(f'La fonction est maximié à {X[l-1, m-1]} \n')

  p = point(X)
  p_s = point_simplifie(A, p)
  print(f'Le point P a les coordonnées {p} ou {p_s} \n')
  
  return X