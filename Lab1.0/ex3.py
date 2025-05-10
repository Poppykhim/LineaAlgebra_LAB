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
