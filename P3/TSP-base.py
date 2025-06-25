from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import pulp

# Cargar el archivo .mat
data = loadmat('usborder.mat')

# Acceder a la estructura 'usbborder'
usbborder = data['usbborder']

# Extraer las variables x, y, xx, yy desde la estructura
x = usbborder['x'][0][0].flatten()
y = usbborder['y'][0][0].flatten()
xx = usbborder['xx'][0][0].flatten()
yy = usbborder['yy'][0][0].flatten()

# Crear un polígono a partir de los puntos x e y
polygon = np.column_stack((x, y))  # Combinar x e y en una matriz de puntos
path = Path(polygon)  # Crear un objeto Path para el polígono

# Configuración inicial
np.random.seed(3)
nStops = 5
stopsLon = np.zeros(nStops)
stopsLat = np.zeros(nStops)
n = 0

# Generar puntos aleatorios dentro del borde de Estados Unidos
while n < nStops:
    xp = np.random.rand() * 1.5
    yp = np.random.rand()
    if path.contains_point((xp, yp)):  # Verificar si el punto está dentro del polígono
        stopsLon[n] = xp
        stopsLat[n] = yp
        n += 1

# Dibujar el borde de Estados Unidos y los puntos de parada
plt.plot(x, y, color='red', label='Borde de Estados Unidos')
plt.scatter(stopsLon, stopsLat, color='blue', marker='*', label='Puntos de parada')
plt.title('Puntos de parada del viajante de comercio')
plt.legend()
plt.show()


####### INCLUIR AQUí EL CÓDIGO DE OPTIMIZACIÓN DEL TSP

# Calcular todas combinaciones
t = nStops * (nStops -1) // 2
P = np.zeros((t,2), dtype=int)
i = 0
j = 1
for n in range(t):
    P[n,0] = i
    P[n,1] = j
    if j == nStops - 1:
        i += 1
        j = i + 1
    else:
        j += 1

# Calcular distancias entre puntos
dist= np.zeros(t)
for n in range(t):
    lat= (stopsLat[P[n,0]] - stopsLat[P[n,1]]) ** 2
    lon= (stopsLon[P[n,0]] - stopsLon[P[n,1]]) ** 2
    dist[n] = np.sqrt(lat + lon)

# Problema de optimizacion
prob = pulp.LpProblem('TSP', pulp.LpMinimize)
# Variables de decicisión (binarias)
x_tsp = [pulp.LpVariable(f'x_{i}', cat='Binary') for i in range(t)]
#Función objetivo
prob += pulp.lpSum([dist[i] * x_tsp[i] for i in range(t)])
# Restricciones
# 1
for k in range(nStops):
    prob += pulp.lpSum([x_tsp[i] for i in range(t) if P[i,0] == k or P[i, 1] == k]) == 2
# 2
prob += pulp.lpSum(x_tsp) == nStops

prob.solve()

x_tsp_sol = np.array([pulp.value(var) for var in x_tsp])

# Encontrar los segmentos de la ruta óptima
segments = np.where(x_tsp_sol == 1)[0]

# Dibujar la ruta óptima
plt.plot(x, y, color='red', label='Borde de Estados Unidos')
plt.scatter(stopsLon, stopsLat, color='blue', marker='*', label='Puntos de parada')
for seg in segments:
    plt.plot([stopsLon[P[seg, 0]], stopsLon[P[seg, 1]]], [stopsLat[P[seg, 0]], stopsLat[P[seg, 1]]], color='green')
plt.title('Solución con subtours')
plt.legend()
plt.show()
