import numpy as np
from scipy.linalg import eigvalsh_tridiagonal, eigvalsh

diagonal = np.array([1.5833333333333332593, -0.01259572752922188954, 2.3690214303404664165, 0.06024096385542132559, 1.9941915593928158934, 1.0058084406071843286])
subdiagonal = np.array([-2.3964673074247340168, 0.93475927884341891705,-2.0788632064407330802, 6.3258425909268308882e-016, -0.075991464158134569562])
eigenvectors = eigvalsh_tridiagonal(diagonal, subdiagonal)
print("Eigenvectors of matrixA to: ")
print(eigenvectors)