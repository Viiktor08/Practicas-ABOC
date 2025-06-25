import numpy as np
import pulp

# Parámetros de entrada
N = 6
M = 3
L = 2
K = 7

# Crear el problema
prob = pulp.LpProblem("RejillaMagica", pulp.LpMinimize)

# Variables: x[i][j] es el valor en la celda (i, j)
x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat="Integer") for j in range(N)] for i in range(N)]

# Restricciones para subrejillas MxL
for i in range(N - M + 1):
    for j in range(N - L + 1):
        prob += pulp.lpSum(x[i + m][j + l] for m in range(M) for l in range(L)) == K

# Restricciones para subrejillas LxM
for i in range(N - L + 1):
    for j in range(N - M + 1):
        prob += pulp.lpSum(x[i + l][j + m] for l in range(L) for m in range(M)) == K

# (Opcional) Función objetivo dummy, ya que solo queremos factibilidad
prob += 0

# Resolver
prob.solve()

# Mostrar la rejilla
rejilla = np.array([[int(pulp.value(x[i][j])) for j in range(N)] for i in range(N)])
print(rejilla)