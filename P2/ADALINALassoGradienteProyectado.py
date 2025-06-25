import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv('hou_all.csv', header=None)

data = data.iloc[:, :-1]

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

scaler_X = StandardScaler()
X=scaler_X.fit_transform(X)
scaler_y=StandardScaler()
y=scaler_y.fit_transform(y.reshape(-1,1)).flatten()

X=np.c_[np.ones(X.shape[0]), X]

k=0

np.random.seed(42)
w=np.random.randn(X.shape[1])

max_iter=100
tolerancia=1e-3
lambda_=100

def norma_l1(w):
    return np.sum(np.abs(w))

def funcion_objetivo(X, y, w, lambda_):
    return 0.5 * np.linalg.norm(X @ w - y) ** 2 + lambda_ * norma_l1(w)

def gradiente(X, y, w):
    return X.T @ (X @ w - y)

def busqueda_linea_backtracking(X, y, w, d, alpha_init=1, beta=0.5):
    alpha = alpha_init
    while funcion_objetivo(X, y, w + alpha * d, lambda_) >= funcion_objetivo(X, y, w, lambda_):
        alpha *= beta
    return alpha

#ALGORITMO DE GRADIENTE PROYECTADO
while k<max_iter:
    grad = gradiente(X, y, w)
    d = -grad
    
    alpha = busqueda_linea_backtracking(X, y, w, d)
    
    w_nuevo = w + alpha * d
    w_nuevo = np.sign(w_nuevo) * np.maximum(np.abs(w_nuevo) - lambda_ * alpha, 0)
    
    if np.linalg.norm(w_nuevo - w) < tolerancia:
        print(f"El algoritmo ha convergido en la iteracion {k}.")
        print(f"Solucion: {w_nuevo}")
        break
    
    w = w_nuevo
    k=k+1

#PREDECIR Y COMPARAR LAS 5 PRIMERAS VIVIENDAS DEL CSV

#Predicción con el modelo aprendido
y_pred_norm = X @ w

#Desnormalizar los valores reales y predichos
y_pred = scaler_y.inverse_transform(y_pred_norm[:5].reshape(-1, 1)).flatten()
y_real = scaler_y.inverse_transform(y[:5].reshape(-1, 1)).flatten()

print("\nComparación de valores reales y predichos para las 5 primeras viviendas:")
for i in range(5):
    print(f"Vivienda {i+1}: Valor real = {y_real[i]:.2f}, Valor predicho = {y_pred[i]:.2f}")


#GRÁFICA DEL NÚMERO DE COEFICIENTES DISTINTOS DE CERO EN FUNCIÓN DE LAMBDA

#Valores de lambda a probar
valores_lambda = [10, 50, 100, 200]
num_coef_no_nulos = []

for lam in valores_lambda:
    # Repetimos entrenamiento para cada lambda
    w = np.random.randn(X.shape[1])
    k = 0
    while k < max_iter:
        grad = gradiente(X, y, w)
        d = -grad
        alpha = busqueda_linea_backtracking(X, y, w, d)
        w_nuevo = w + alpha * d
        w_nuevo = np.sign(w_nuevo) * np.maximum(np.abs(w_nuevo) - lam * alpha, 0)

        if np.linalg.norm(w_nuevo - w) < tolerancia:
            break

        w = w_nuevo
        k += 1

    num_no_nulos = np.sum(w != 0)
    num_coef_no_nulos.append(num_no_nulos)

# Graficar
plt.figure(figsize=(8,5))
plt.plot(valores_lambda, num_coef_no_nulos, marker='o')
plt.xlabel(r'$\lambda$ (regularización)', fontsize=12)
plt.ylabel('Número de coeficientes distintos de cero', fontsize=12)
plt.title('Efecto de $\lambda$ en la selección de características', fontsize=14)
plt.grid(True)
plt.savefig('grafica_lambda_vs_coeficientes.png')
plt.show()