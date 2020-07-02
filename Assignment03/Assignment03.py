import numpy as np
import matplotlib.pyplot as plt


# Calculate Ket phi
def get_phi(k0, k1, n, phi):
    i = np.complex(0, 1)
    result = 1
    for k in reversed(range(n)):
            a = (1 / np.sqrt(2)) * (k0 + (np.exp(2 * np.pi * i * (2 ** k) * phi) * k1))
            result = np.kron(result, a)
    return result

# Calculate the complex conjugate of F
def get_F(N):
    i = np.complex(0, 1)
    s = 0
    for k in range(N):
        for l in range(N):
            ket_k = np.zeros((N, 1))
            ket_l = np.zeros((N, 1))
            np.put(ket_k, k, 1)
            np.put(ket_l, l, 1)
            e = np.exp((-2 * np.pi * i * k * l) / N)
            s += e * np.outer(ket_l, ket_k.T)
    
    return (1 / np.sqrt(N)) * s  
			

# Initialize N
n = 5
N = 2 ** n

# Initialize Ket Zero and Ket One
ket_zero = np.array([[1],[0]])
ket_one = np.array([[0],[1]])

# Calculate F
F = get_F(N)

l = []
for j in range(N):
    phi = float(j / 256)
    ket_phi = get_phi(ket_zero, ket_one, n, phi)
    qstate =  np.matmul(F, ket_phi)
    qstate = np.abs(np.real(qstate))
    print(np.abs(np.real(qstate)))	
    l.append(qstate)
    
x = range(N)

for k in range(30, 41):
    Px = l[k - 30].tolist()
    print(f'phi: {k}/256')
    plt.plot(x, Px, 'o', label='Pr(x)')
    plt.ylim((0,1.1))
    plt.legend()
    plt.show()
