import cmath
import numpy as np 

# Initialize imaginary number 
i = complex(0, 1)

# Pauli Operators
sigma_x = np.matrix([[0, 1], [1, 0]])
sigma_y = np.matrix([[0, -i], [i, 0]])
sigma_z = np.matrix([[1, 0], [0, -1]])

# Calculate Eigenvalues of Pauli Operators
eigen_val_x = np.linalg.eigvals(sigma_x)
eigen_val_y = np.linalg.eigvals(sigma_y)
eigen_val_z = np.linalg.eigvals(sigma_z)

eigen_vec_x = np.linalg.eig(sigma_x) 
eigen_vec_y = np.linalg.eig(sigma_y)
eigen_vec_z = np.linalg.eig(sigma_z)

print("The Eigenvalues for sigma_x: ")
print(eigen_val_x)
print("The Eigenvalues for sigma_y: ")
print(eigen_val_y)
print("The Eigenvalues for sigma_z: ")
print(eigen_val_z)    

print("The Eigenvectors for sigma_x: ")
print(eigen_vec_x)
print("The Eigenvectors for sigma_y: ")
print(eigen_vec_y)
print("The Eigenvectors for sigma_z: ")
print(eigen_vec_z)  