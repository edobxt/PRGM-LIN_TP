# PRGM-LIN TP DU 11/04/22
# KANCEL JONATHAN - BARVAUT TEDDRICE

import numpy as np
from simplexe import simplexe

A = np.array([
  [1, 2, 1, 0, 0, 0, 120],
  [1, 1, 0, 1, 0, 0, 100],
  [1, 0, 0, 0, 1, 0, 70],
  [0, 1, 0, 0, 0, 1, 50],
  [20, 10, 0, 0, 0, 0, 0]
])

print(f'Simplexe de base = \n {A} \n')

X = simplexe(A)
