import numpy as np

B = np.array([[1, 7,-3], [1, 3,1],[4,8,1]])

det_B = np.linalg.det(B)    

B_afterSwap = np.array([[1, 3,1],[1, 7,-3],[4,8,1]])

det_B_afterSwap = np.linalg.det(B_afterSwap)  


print("Determinant of B:", det_B)
print("Determinant of B_afterSwap:", det_B_afterSwap)

# det(B swapped​)=−det(B)
