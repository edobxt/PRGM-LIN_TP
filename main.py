# PRGM-LIN TP DU 11/04/22
# KANCEL JONATHAN - BARVAUT TEDDRICE

import numpy as np
from simplexe import simplexe

A = np.array([
  [0, -12, -4, 1, 0, 5, 0],
  [0, 0, 1, 0, 1, 0, 5],
  [1, 3, 1, 0, 0, -1, 3],
  [0, -29, 20, 0, 0, 10, -30]
])

print(f'Simplexe de base = \n {A} \n')

X = simplexe(A)
print(f'Tableau final = \n {X}')