import numpy as np

print("Exercise Compute the solutions to the matrix equation Bx = b(using the B defined earlier).")

B = np.matrix([[14, -2, 12],
               [4, 4, 5],
               [5, 5, 1]])

b = np.matrix([[-1], [2], [1]])

x = np.linalg.solve(B, b)

print("B = \n", B, "\n")
print("b = \n", b, "\n")
print("Answer Bx = b:\n")
print(x)

print("\nExercise compute the inverse and determinant of B (defined previously).")
print("\nInverse of B\n")

Binv = np.linalg.inv(B)
Binv = np.round(Binv, 2)

print(Binv)

print("\nDeterminant of B\n")

BDet = np.linalg.det(B)

print("|B| = ", BDet)
