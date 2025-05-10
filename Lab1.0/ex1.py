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
