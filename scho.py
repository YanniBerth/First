import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar
from scipy.linalg import eigh

# Definir parámetros
N = 1000  # Número de puntos
L = 10.0  # Longitud del pozo
x = np.linspace(-L, L, N)
dx = x[1] - x[0]

# Matriz de energía cinética
T = -hbar**2 / (2 * dx**2) * (-2 * np.eye(N) + np.eye(N, k=1) + np.eye(N, k=-1))

# Potencial del oscilador armónico
V = 0.5 * x**2
V_matrix = np.diag(V)

# Hamiltoniano
H = T + V_matrix

# Resolver la ecuación de Schrödinger
eigenvalues, eigenstates = eigh(H)

# Graficar los primeros tres estados
for i in range(3):
    plt.plot(x, eigenstates[:, i], label=f"Estado {i}")
    
plt.title('Funciones de onda del oscilador armónico cuántico')
plt.xlabel('Posición')
plt.ylabel('Función de onda')
plt.legend()
plt.show()
