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
    bra_x = np.zeros((d, 1))
    ket_x = np.zeros((d, 1))
    np.put(bra_x, (k % d), 1)
    np.put(ket_x, ((k + 1) % d), 1)
    x = np.add(x, np.outer(ket_x, bra_x))

# Build matrix Z. 
for l in range(0, d):
    bra_z = np.zeros((d, 1))
    ket_z = np.zeros((d, 1))
    np.put(bra_z, (l % d), 1)
    np.put(ket_z, (l % d), 1)
    z = np.add(z, np.multiply((omega ** l), np.outer(ket_z, bra_z)))
print("X:")
print(x)
print("Z:")
print(z)

# Raise Matrices X, Z by powers a, b respectifully 
# where a, b are elements of the set {0, 1, ... , d - 1}
# Then calculate the trace inner product of all combinations of the pairs,
# X^a, Z^b.
for a in range(0, d):
    for b in range(0, d):
        m = np.multiply(np.linalg.matrix_power(x, a), np.linalg.matrix_power(z, b))
        print(np.trace(m))

if success:
    print("Hooray!")
else: 
    print("You suck!")
