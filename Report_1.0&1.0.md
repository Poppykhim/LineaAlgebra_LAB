# Lab01

## Exercise 1: Calculate -2E, G + F, 4F – G, HG, and GE using the following matrix definitions. Do the exercise on paper first, then check by doing the calculation with NumPy arrays.

## Source Code

```python
import numpy as np

print("Calculate -2E, G + F, 4F - G, HG, and GE using the following matrix definitions. Do the " \
"exercise on paper first, then check by doing the calculation with NumPy arrays.\n")

E = np.matrix("5;-2")
F = np.matrix("1, 6; 2, 0; -1, -1")
G =  np.matrix("2, 0; -1, 3; -1, 6")
H = np.matrix("3, 0, 1; 1, -2, 2; 3, 4, -1")
print("E = \n", E, "\nF = \n", F, "\nG = \n", G, "\nH = \n", H)

print("\t\t\t\nAnwer\n")

answer_1 = (-2) * E
print("Answer -2E = \n\n", answer_1, "\n")

answer_2 = np.add(G, F)
print("Answer G + F = \n\n", answer_2, "\n")

answer_3= (4) * F - G
print("Answer 4F-G = \n\n", answer_3, "\n")

answer_4 = H@G
print("Answer HG=\n\n", answer_4, "\n")

answer_5 = G@E
print("Answer GE=\n\n", answer_5, "\n")

```

## Output

```python
Calculate -2E, G + F, 4F - G, HG, and GE using the following matrix definitions. Do the exercise on paper first, then check by doing the calculation with NumPy arrays.

E = [[ 5]
     [-2]]

F = [[ 1  6]
     [ 2  0]
     [-1 -1]]

G = [[ 2  0]
     [-1  3]
     [-1  6]]

H = [[ 3  0  1]
     [ 1 -2  2]
     [ 3  4 -1]]

Anwer:

Answer -2E = [[-10]
              [  4]]

Answer G + F =[[ 3  6]
               [ 1  3]
               [-2  5]]

Answer 4F-G = [[  2  24]
               [  9  -3]
               [ -3 -10]]

Answer HG= [[5 6]
            [2 6]
            [3 6]]

Answer GE= [[ 10]
            [-11]
            [-17]]

```

## Exercise 2: Define NumPy arrays for the matrices H and G given below.

#### (a) Multiply the second and third column of H with the first and second row of G. Use slicing to make subarrays. Does the result have any relationship to the full product HG?

#### (b) Multiply the first and second row of H with the second and third column of G. Does this result have any relationship to the full product HG?

## Source Code

```python
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

H_row = H[0:2,:]
G_column = G[:, 1:3]
result_2 = np.dot(H_row, G_column)

print("\n(b). Answer")
print("Result of multiplying selected columns and rows:\n")
print(result_2)
print("\nCorresponding block from full product HG:\n")
print(full_product[0:2, 1:3])
print("\nThus, since the result matches the full product of H and G, it has a relationship with the full product HG.")

```

## Output

```python
Full Product HG:

[[ 22   7  -7 -15]
 [ 13   1  26  57]
 [ 53   3   4  27]]

(a). Answer
Result of multiplying selected columns and rows:

[[ -4  17   9  -9]
 [ 56 -16 -24   0]
 [ 41  20  -3 -18]]

Corresponding block from full product HG:

[[ 7 -7]
 [ 1 26]]

Thus, there is no direct relationship between the subarray result and the full product HG.

(b). Answer
Result of multiplying selected columns and rows:

[[ 7 -7]
 [ 1 26]]

Corresponding block from full product HG:

[[ 7 -7]
 [ 1 26]]

Thus, since the result matches the full product of H and G, it has a relationship with the full product HG.
```

## Exercise 3: Generate a 4 x 4 matrix B with random integer entries. Compute matrices P = ½(B+BT) and Q = 1/2(B-BT). Rerun your code several times to get different matrices. What do you notice about P and Q? Explain why it must always be true.

## Source Code

```python

import numpy as np

B = np.random.randint(-10, 10, size=(4, 4))
print("Matrix B:")
print(B)

P = 0.5 * (B + B.T)
Q = 0.5 * (B - B.T)

print("\nMatrix P (Symmetric part):")
print(P)

print("\nMatrix Q (Skew-symmetric part):")
print(Q)

print("\nP is symmetric:", np.allclose(P, P.T))
print("Q is skew-symmetric: ", np.allclose(Q, -Q.T))

```

## Output

```python
Matrix B:
[[  2   6   8  -2]
 [ -8 -10  -8  -1]
 [  9   6   1   1]
 [-10   5  -4   5]]

Matrix P (Symmetric part):
[[  2.   -1.    8.5  -6. ]
 [ -1.  -10.   -1.    2. ]
 [  8.5  -1.    1.   -1.5]
 [ -6.    2.   -1.5   5. ]]

Matrix Q (Skew-symmetric part):
[[ 0.   7.  -0.5  4. ]
 [-7.   0.  -7.  -3. ]
 [ 0.5  7.   0.   2.5]
 [-4.   3.  -2.5  0. ]]

P is symmetric: True
Q is skew-symmetric:  True
```

# Lab1.1

## Exercise: Compute the solution to the matrix equation Bx = b(using the B defined earlier).

```python
B = ([[14, -2, 12],
      [4, 4, 5],
      [5, 5, 1]])

b = ([[-1],
     [2],
     [1]])
```

## Exercise: Compute the inverse and determinant of B(defined previously).

## Source Code

```python
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

```

## Output

```python
Exercise Compute the solutions to the matrix equation Bx = b(using the B defined earlier).
B =
 [[14 -2 12]
 [ 4  4  5]
 [ 5  5  1]]

b =
 [[-1]
 [ 2]
 [ 1]]

Answer Bx = b:

[[-0.25892857]
 [ 0.40178571]
 [ 0.28571429]]

Exercise compute the inverse and determinant of B (defined previously).

Inverse of B

[[ 0.06 -0.18  0.17]
 [-0.06  0.14  0.07]
 [-0.    0.24 -0.19]]

Determinant of B

|B| =  -336.0
```
