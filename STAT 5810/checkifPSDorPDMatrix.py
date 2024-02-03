import numpy as np

A_Matrix = np.array([[1,-2], [3,4], [-5,6]])
B_Matrix = np.array([[1,0,0], [0,1,0], [0,0,1]])
negB_Matrix = np.array([[-1,0,0], [0,-1,0], [0,0,-1]])
C_Matrix = np.array([[2,2,1], [2,3,2], [1,2,2]])

def is_positive_definite(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return all (eig > 0 for eig in eigenvalues)

def is_positive_semi_definite(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return all (eig >= 0 for eig in eigenvalues)

AAt = A_Matrix.dot(A_Matrix.transpose())

print(AAt)
print(np.linalg.eigvals(AAt))

if is_positive_definite(AAt):
    print("The matrix is positive definite.")
elif is_positive_semi_definite(AAt):
    print("The matrix is positive semi-definite.")
else:
    print("The matrix is neither positive definite nor positive semi-definite.")

print(np.linalg.eigvals(B_Matrix))
print(np.linalg.eigvals(C_Matrix))
print(np.linalg.eigvals(C_Matrix+B_Matrix))