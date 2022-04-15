# PRGM-LIN TP DU 11/04/22
# KANCEL JONATHAN - BARVAUT TEDDRICE

import numpy as np
from simplexe import simplexe

A = np.array([
    [-3, 2, 1, 0, 0, 0, 2], 
    [-1, 2, 0, 1, 0, 0, 4], 
    [1, 1, 0, 0, 1, 0, 5],
    [0, 1, 0, 0, 0, 1, 50],
    [-1, -2, 0, 0, 0, 0, 0],
])
print(f'Simplexe = \n {A} \n')

X = simplexe(A)
#X = ratio(A, 0)
print(f'Resultat = \n {X}')