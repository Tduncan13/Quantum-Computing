import numpy as np
import matplotlib.pyplot as plt

# Initialize complex number.
i = complex(0, 1)

# Initialize Ket Vectors.
k0 = np.array([[1],[0]])
k1 = np.array([[0],[1]])

# Initialize test unitiary gates. 
h = (1 / np.sqrt(2)) * np.array([[1, 1],[1, -1]])
x = np.array([[0, 1],[1, 0]])
y = np.array([[0, -i],[i, 0]])
z = np.array([[1, 0], [0, -1]])

# Perform Hadamard Test to calculate probabilities. 
def hadamard_test(q, u):
    a = np.matmul(u, q)
    b = q.T.dot(a)
    return (0.5 * np.asscalar(1 + np.real(b)), 0.5 * np.asscalar(1 - np.real(b)))

# Determine the probabilities for U = X (bit flip) and ket_plus and ket_minus. 
zero, one = hadamard_test(k0, x)
print("Probability for Zero given Ket Zero: %.2f%%" % zero)
print("Probability for One given Ket Zero: %.2f%%" % one)
zero, one = hadamard_test(k1, x)
print("Probability for Zero given Ket One: %.2f%%" % zero)
print("Probability for One given Ket One: %.2f%%" % one)

# Calculate the probabilities for U = diag(1, e^(2PIiv)) for v = [0, 1) and q = k1
trials = 10
probs_zero = []
probs_one = []
for n in range(trials):
    e = np.array([[1, 0],[0, np.exp(2 * np.pi * i * (float(n) / trials))]])
    zero, one = hadamard_test(k1, e)
    probs_zero.append(zero)
    probs_one.append(one)

# Plot results. 
y_axis = np.arange(0, 100, 10)
plt.plot(probs_zero, y_axis)
plt.plot(probs_one, y_axis)
plt.xlabel('Phi Value')
plt.ylabel('Probability')
plt.title('Probability of Measuring a Zero or a One as Phi Approaches One.')
plt.show()
