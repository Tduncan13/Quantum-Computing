import cmath
import numpy as np 

# Set success flag. 
success = True

# Initialize imaginary number 
i = complex(0, 1)

# Initialize Pauli Operators
sigma_x = np.matrix([[0, 1], [1, 0]])
sigma_y = np.matrix([[0, -i], [i, 0]])
sigma_z = np.matrix([[1, 0], [0, -1]])

# Calculate Eigenvalues and Eignevectors of Pauli Operators 
eigen_val_x, eigen_vec_x = np.linalg.eig(sigma_x) 
eigen_val_y, eigen_vec_y = np.linalg.eig(sigma_y)
eigen_val_z, eigen_vec_z = np.linalg.eig(sigma_z)

# Get value of d
rows, d = eigen_vec_x.shape

# Check if mutually unbiased. 
for n in range(0, d):
    for m in range(0, d):

        # Compute inner product on all combinations of 
        # Pauli Operator Eigenvectors
        result_x_y = np.inner(eigen_vec_x[n], eigen_vec_y[m])
        result_x_z = np.inner(eigen_vec_x[n], eigen_vec_z[m])
        result_y_x = np.inner(eigen_vec_y[n], eigen_vec_x[m])
        result_y_z = np.inner(eigen_vec_y[n], eigen_vec_z[m])
        result_z_x = np.inner(eigen_vec_z[n], eigen_vec_x[m])
        result_z_y = np.inner(eigen_vec_z[n], eigen_vec_y[m])
       
        # Calculate testing value on all combinations. 
        test_x_y = np.abs(result_x_y.item(0)) ** 2
        test_x_z = np.abs(result_x_z.item(0)) ** 2
        test_y_x = np.abs(result_y_x.item(0)) ** 2
        test_y_z = np.abs(result_y_z.item(0)) ** 2
        test_z_x = np.abs(result_z_x.item(0)) ** 2
        test_z_y = np.abs(result_z_y.item(0)) ** 2

        # Check if resulting value is equal to 1/d
        if np.round(test_x_y, decimals=1, out=None) != 1 / d:
            success == False
        if np.round(test_x_z, decimals=1, out=None) != 1 / d:
            success == False
        if np.round(test_y_x, decimals=1, out=None) != 1 / d:
            success == False
        if np.round(test_y_z, decimals=1, out=None) != 1 / d:
            success == False
        if np.round(test_z_x, decimals=1, out=None) != 1 / d:
            success == False
        if np.round(test_z_y, decimals=1, out=None) != 1 / d:
            success == False
  
if not success:
    print("You Suck!")
else:
    print("Hooray!")
