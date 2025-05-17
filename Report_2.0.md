<p>
  <img src="ITC.gif" alt="Alt text" style="float: left; width: 220px; margin-right: 20px;">
Name: Virak Rith

Student ID: P20230033

Course: Linear Algebra and Statistics for Engineers

Instructor: PHAUK Sokkhey

Assignment: Lab2.0(1-4)

Due Date: May 18, 2025 (12:00 AM)

</p>
<br/>

# Exercise 1: Determinant of a 2x2 Matrix Compute the determinant of the following matrices:

```python
A= [[2 3]
    [4 1]]
b= [[-1 5]
    [ 3 2]]
```

Hint: Use np. Linalg.det()

## Source Codes

```py
import numpy as np

A = np.array([[2, 3,], [4, 1]])
B = np.array([[-1, 5], [3, 2]])

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

print("Determinant of A:", det_A)
print("Determinant of B:", det_B)
```

## Output

```py
Determinant of A: -10.000000000000002
Determinant of B: -17.0
```

---

# Exercise 2: Compute Determinants Given the matrix:

```py
B= [[ 1  7 -3]
    [ 1  3  1]
    [ 4  8  1]]
```

## Compute the determinant using np.linalg.det(). Observe what happens if you swap row 1 and 2 , and recompute the determinant.

Hint: Swapping rows changes the sign of the determinant.

## Source Code

```C++
import numpy as np

B = np.array([[1, 7,-3], [1, 3,1],[4,8,1]])

det_B = np.linalg.det(B)

B_afterSwap = np.array([[1, 3,1],[1, 7,-3],[4,8,1]])

det_B_afterSwap = np.linalg.det(B_afterSwap)


print("Determinant of B:", det_B)
print("Determinant of B_afterSwap:", det_B_afterSwap)
```

## Output:

```py
Determinant of B: 27.999999999999996
Determinant of B_afterSwap: -27.999999999999996
```

---

# Exercise 3: Compute Minors and Cofactors Given matrix:

```py
C= ⎡1  3⎤
   ⎢    ⎥
   ⎣2  4⎦
```

### Use sympy.Matrix to:

1. Print the matrix of minors.
2. Print the matrix of cofactors.
   Hint: Use .minor (i,j) and .cofactor( i,j ) from sympy.Matrix

## Source Code:

```python
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
```

## Output:

```py
Matrix of Minors:

⎡4  2⎤
⎢    ⎥
⎣3  1⎦

Matrix of Cofactors:

⎡4   -2⎤
⎢      ⎥
⎣-3  1 ⎦
```

---

# Exercise 4: Given the matrix A :

```py
 A =[[1 2 3 4]
     [5 6 7 8]
     [2 6 4 8]
     [3 1 1 2]]
```

1. Import the required modules from SciPy and NumPy.
2. Check if matrix A is invertible by calculating its determinant.
3. If invertible, compute the inverse matrix

## Source Code:

```py
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
```

## Output:

```py
Determinant of A: 72.0
Inverse of A:
 [[-0.16666667  0.05555556 -0.05555556  0.33333333]
 [-0.83333333  0.27777778  0.22222222 -0.33333333]
 [ 0.16666667  0.27777778 -0.27777778 -0.33333333]
 [ 0.58333333 -0.36111111  0.11111111  0.33333333]]
```

## Link to GitHub Account : [Click Here](https://github.com/Poppykhim/LineaAlgebra_LAB.git) <3

Note: Viewing in VsCode IDE for better formatting!!!
