import numpy as np
from scipy.linalg import det, inv

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [2, 6, 4, 8],
    [3, 1, 1, 2]
])
det_A = det(A)
print("Determinant of A:", det_A)

if abs(det_A) != 0:
    A_inv = inv(A)
    print("Inverse of A:\n", A_inv)
else:
    print("Matrix A is not invertible.")
