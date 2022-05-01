from maximal import maximal
from pivot import pivot
from ratio import ratio

def simplexe(A):
  # copie du simplexe afin d'effectuer les opérations
  X = A.copy()
  nb_pivotement = 1

  # tant qu'il y a des positifs sur la dernière ligne
  while X[X.shape[0]-1, maximal(X)] > 0:
    # récupération de la ligne et de la colonne pivot
    index_colonne_pivot = maximal(X)
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
  return X