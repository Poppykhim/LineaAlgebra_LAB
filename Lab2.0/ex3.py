import sympy as sy

C = sy.Matrix([
    [1, 3],
    [2, 4]
])

# Matrix of minors
minors = C.minor_submatrix(0, 0).det(), C.minor_submatrix(0, 1).det(), \
         C.minor_submatrix(1, 0).det(), C.minor_submatrix(1, 1).det()
print(minors)
minors_matrix = sy.Matrix(2, 2, minors)
print("\nMatrix of Minors:")
sy.pprint(minors_matrix)

# Matrix of cofactors
cofactors_matrix = sy.Matrix([
    [C.cofactor(0, 0), C.cofactor(0, 1)],
    [C.cofactor(1, 0), C.cofactor(1, 1)]
])

print("\nMatrix of Cofactors:")
sy.pprint(cofactors_matrix)
