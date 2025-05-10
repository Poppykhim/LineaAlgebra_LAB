import numpy as np

H = np.array([[3, 3, -1], [-3, 0, 8], [1, 6, 5]])
G = np.array([[1, 5, 2, -3], [7, -2, -3, 0], [2, 2, 4, 6]])

full_product = np.dot(H, G)
print("Full Product HG:\n")
print(full_product)

# Multiply the second and third column of H with the first and second row of G. Use slicing to make subarryas. Does the result have any relationship to the full product HG?

H_column = H[:, 1:3]
G_row = G[0:2, :]
result_1 = np.dot(H_column, G_row)

print("\n(a). Answer")
print("Result of multiplying selected columns and rows:\n")
print(result_1)
print("\nCorresponding block from full product HG:\n")
print(full_product[0:2, 1:3])
print("\nThus, there is no direct relationship between the subarray result and the full product HG.")

# Multiply the first and second row of H with the second and third column of G. Does this result have any relationship to the full product HG?

H_row = H[0:2,:]
G_column = G[:, 1:3]
result_2 = np.dot(H_row, G_column)

print("\n(b). Answer")
print("Result of multiplying selected columns and rows:\n")
print(result_2)
print("\nCorresponding block from full product HG:\n")
print(full_product[0:2, 1:3])
print("\nThus, since the result matches the full product of H and G, it has a relationship with the full product HG.")
