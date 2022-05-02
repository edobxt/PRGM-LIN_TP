# PRGM-LIN TP DU 11/04/22
# KANCEL JONATHAN - BARVAUT TEDDRICE

import numpy as np
from simplexe import simplexe
from point import point

A = np.array([
  [0, -12, -4, 1, 0, 5, 0],
  [0, 0, 1, 0, 1, 0, 5],
  [1, 3, 1, 0, 0, -1, 3],
  [0, -29, 20, 0, 0, 10, -30]
])

B = np.array([
  [1, 2, 1, 0, 0, 0, 120],
  [1, 1, 0, 1, 0, 0, 100],
  [1, 0, 0, 0, 1, 0, 70],
  [0, 1, 0, 0, 0, 1, 50],
  [20, 10, 0, 0, 0, 0, 0]
])

print(f'Simplexe de base = \n {B} \n')

X = simplexe(B)
#print(f'Tableau final = \n {X}')

point(X)