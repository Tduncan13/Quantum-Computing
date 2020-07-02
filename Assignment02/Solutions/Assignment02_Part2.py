#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Initialize complex number.
i = np.complex(0, 1)


# Initialize Ket Vectors.
k0 = np.array([[1], [0]])
k1 = np.array([[0], [1]])
k_plus = (1 / np.sqrt(2) * (k0 + k1))
k_minus = (1 / np.sqrt(2) * (k0 - k1))


# Initiatlize test unitary gates.
x = np.array([[0, 1], [1, 0]])
y = np.array([[0, -i], [i, 0]])
z = np.array([[1, 0], [0, -1]])

# Define the Hadamard Gate.
def hadamard_gate(d):
    h = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    return np.kron(h, np.identity(d))

# Define projector.
def projector(k, d):
    return np.kron(k * k.T, np.identity(d))


# Define the Swap Gate. 
def swap_gate(k0, k1):
    k_0 = np.kron(k0, k0) * np.kron(k0.T, k0.T)
    k_1 = np.kron(k0, k1) * np.kron(k1.T, k0.T)
    k_2 = np.kron(k1, k0) * np.kron(k0.T, k1.T)
    k_3 = np.kron(k1, k1) * np.kron(k1.T, k1.T)
    S = k_0 + k_1 + k_2 + k_3
    return np.kron(k0 * k0.T, np.identity(4)) + np.kron(k0 * k0.T, S)

def swap_test(k0, k1, psi, phi):
    H = hadamard_gate(4)
    S = swap_gate(k0, k1)
    p0 = projector(k0, 4)
    p1 = projector(k1, 4)
    psi_prime = np.kron(psi, phi)
    state_1 = np.kron(k0, psi_prime)
    state_2 = np.dot(H, state_1)
    state_3 = np.dot(S, state_2)
    state_4 = np.dot(H, state_3)

    return get_probability(p0, p1, 0, state_4)

def get_probability(p0, p1, val, state):
    if val == 0:
        return np.linalg.norm(np.dot(p0, state), 2) ** 2
    else:
        return np.linalg.norm(np.dot(p1, state), 2) ** 2

# We perform the Swap Test on the inputs psi = k0 and phi = k0. 
# Since the inputs are the same we should expect the Swap Test to return the probability 100%
print('Perfroming Swap Test: psi = ket(0), phi = ket(0)')
prob = np.ceil(swap_test(k0, k1, k0, k0) * 100)
if prob == 100.0:
    print(f'Swap Test Successful! Probability: {prob}')
elif prob == 50.0:
    print(f'Swap Test Failed! Probability: {prob}')
else:
    print(f'Swap Test Uncertainty. Probability: {prob}')

# We perform the Swap Test on the inputs psi = k1 and phi = k1. 
# Since the inputs are the same we should expect the Swap Test to return the probability 100%
print('Perfroming Swap Test: psi = ket(1), phi = ket(1)')
prop = np.ceil(swap_test(k0, k1, k1, k1) * 100)
if prob == 100.0:
    print(f'Swap Test Successful! Probability: {prob}')
elif prob == 50.0:
    print(f'Swap Test Failed! Probability: {prob}')
else:
    print(f'Swap Test Uncertainty. Probability: {prob}')

# We perform the Swap Test on the inputs psi = k0 and phi = k0. 
# Since the inputs are the same we should expect the Swap Test to return the probability 100%
print('Perfroming Swap Test: psi = ket(0), phi = ket(1)')
prob = np.ceil(swap_test(k0, k1, k0, k1) * 100)
if prob == 100.0:
    print(f'Swap Test Failed! Probability: {prob}')
elif prob == 50.0:
    print(f'Swap Test Successful! Probability: {prob}')
else:
    print(f'Swap Test Uncertainty. Probability: {prob}')

# We will test the effect of varying phi and keeping theta constant. 
probabilities_phi = []

trials = 100
for phi in range(trials):
    for theta in range(1):
        psi_big = (np.sin(2 * np.pi * (float(theta) / trials)) * k0) + (np.exp(2 * np.pi * i * (float(phi) / trials)) * np.cos( 2 * np.pi * (float(theta) / trials)) * k1)
        prob = swap_test(k0, k1, k0, psi_big)
        probabilities_phi.append(prob)

# Plot results.
# You will notice that the probability remains constant as phi approaces 1
phi_values = np.arange(0, 1, 0.01)
plt.plot(phi_values, probabilities_phi, label='Probability of Success')
plt.xlabel('Theta Value')
plt.ylabel('Probability')
plt.title('Probability of Swap Test Success.')
plt.legend()
plt.show()


# Next we test we will test the opposite approach. Keep phi constant and allow theta to vary. 
probabilities_phi = []

trials = 100
for theta in range(trials):
    for phi in range(1):
        psi_big = (np.sin(2 * np.pi * (float(theta) / trials)) * k0) + (np.exp(2 * np.pi * i * (float(phi) / trials)) * np.cos( 2 * np.pi * (float(theta) / trials)) * k1)
        prob = swap_test(k0, k1, k0, psi_big)
        probabilities_phi.append(prob)

# Plot results.
# Notice when theta approaches 1, the probabilities oscillate between 50% and 100% event with 
# phi remaining constant.  This remains true for any value of phi as theta varies.  This information
# tells us that e^(2 * pi * theta) is doing little to contribute to the test.
phi_values = np.arange(0, 1, 0.01)
plt.plot(phi_values, probabilities_phi, label='Probability of Success')
plt.xlabel('Theta Value')
plt.ylabel('Probability')
plt.title('Probability of Swap Test Success.')
plt.legend()
plt.show()
