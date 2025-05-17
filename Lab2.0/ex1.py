import numpy as np

A = np.array([[2, 3,], [4, 1]])
B = np.array([[-1, 5], [3, 2]])
  
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

print("Determinant of A:", det_A)
print("Determinant of B:", det_B)
