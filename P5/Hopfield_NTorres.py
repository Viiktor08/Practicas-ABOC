import numpy as np
import matplotlib.pyplot as plt
import copy

# Dimensión del tablero (N x N)
N = 6  # Puedes cambiar el tamaño aquí

# Total de unidades (una por celda del tablero)
num_celdas = N * N

# Generación del estado inicial aleatorio (0 = vacío, 1 = torre)
configuracion = np.random.choice([0, 1], size=num_celdas)

def evaluar_energia(config, N, alpha=1, beta=1):
    energia = 0
    tablero = config.reshape((N, N))

    for fila in range(N):
        suma_fila = np.sum(tablero[fila, :])
        energia += alpha * (suma_fila - 1) ** 2

    for columna in range(N):
        suma_columna = np.sum(tablero[:, columna])
        energia += beta * (suma_columna - 1) ** 2

    return energia

def hopfield_dinamica(config, N, max_pasos=1000):
    estado = copy.deepcopy(config)
    registro_energia = []

    for paso in range(max_pasos):
        energia_actual = evaluar_energia(estado, N)
        registro_energia.append(energia_actual)
        modificado = False

        for idx in range(len(estado)):
            candidato = copy.deepcopy(estado)
            candidato[idx] = 1 - candidato[idx]

            energia_nueva = evaluar_energia(candidato, N)

            if energia_nueva < energia_actual:
                estado[idx] = candidato[idx]
                modificado = True
                break  # Solo una neurona por iteración

        if not modificado:
            break

    return estado, registro_energia

# Energía inicial
energia_inicial = evaluar_energia(configuracion, N)
print(f"\nEstado inicial - Energía: {energia_inicial}")
print(configuracion.reshape((N, N)))

# Evolución de la red
resultado, historia = hopfield_dinamica(configuracion, N)

# Energía final
energia_final = evaluar_energia(resultado, N)
print(f"\nEstado final - Energía: {energia_final}")
print(resultado.reshape((N, N)))
print(f"\nIteraciones ejecutadas: {len(historia)}")

def dibujar_tablero_con_bordes(config, N, titulo="Tablero Visual"):
    print(f"\n{titulo}\n")

    tablero = config.reshape((N, N))

    linea_horizontal = "+" + "---+" * N
    for i in range(N):
        print(linea_horizontal)
        fila = "|"
        for j in range(N):
            celda = "T " if tablero[i, j] == 1 else "  "
            fila += f" {celda}|"
        print(fila)
    print(linea_horizontal)


dibujar_tablero_con_bordes(configuracion, N, titulo="Tablero Inicial con Bordes")
dibujar_tablero_con_bordes(resultado, N, titulo="Tablero Final con Bordes")



def verificar_solucion(config, N):
    
    tablero = config.reshape((N, N))
    for i in range(N):
        if np.sum(tablero[i, :]) != 1:
            return False
        if np.sum(tablero[:, i]) != 1:
            return False
    return True

es_valida = verificar_solucion(resultado, N)
print(f"\n{'SI' if es_valida else 'No'} es solución válida ")
