import cmath
import numpy as np

# Set success flag
success = True

# Initialize variables
i = complex(0, 1)
d = 2
omega = np.exp((2 * np.pi * i) / d)

# Initialize matrix X and Z.
x = np.zeros(d)
z = np.zeros(d)

# Build matrix X.
for k in range(0, d):
    bra = np.zeros((d, 1))
    ket = np.zeros((d, 1))
    np.put(bra, (k % d), 1)
    np.put(ket, ((k + 1) % d), 1)
    x = np.add(x, np.outer(ket, bra))
    print("x")
    print(x)

# Build matrix Z. 
for l in range(0, d):
    bra = np.zeros((d, 1))
    ket = np.zeros((d, 1))
    np.put(bra, (k % d), 1)
    np.put(ket, (k % d), 1)
    z = np.add(z, np.multiply((omega ** l), np.outer(ket, bra)))
    print("z")
    print(z)

for a in range(0, d):
    for b in range(0, d):
        m = np.multiply(np.linalg.matrix_power(x, a), np.linalg.matrix_power(z, b))
        eig_val_m, eig_vec_m = np.linalg.eig(m)
        eig_val_xz, eig_val_xz = np.linalg.eig()
        result = np.inner(m, np.trace(np.inner(np.linalg.matrix_power(x, a), np.linalg.matrix_power(z, b))))
        print("result")
        print(result)
