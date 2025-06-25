import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

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

tolerance=1e-3

max_iter=1000

def compute_gradient(X, y, w):
    return X.T @ (X @ w - y)

def compute_step_size(X,d):
    return (d.T @ d)/(d.T @ X.T @ X @ d)

def compute_error(X, y, w):
    return np.linalg.norm(X @ w - y)**2

#ALGORITMO DE DESCENSO DE GRADIENTE
while k < max_iter:
    gradient=compute_gradient(X, y, w)
    error=compute_error(X, y, w)
    print(f"Iteracion {k}: Error = {error:.6f} // Norma del gradiente = {np.linalg.norm(gradient):.6f}")

    if np.linalg.norm(gradient) <= tolerance:
        print(f"El algoritmo ha convergido en la iteracion {k}.")
        print(f"Solucion: {w}")
        break

    d=-gradient
    alpha=compute_step_size(X,d)
    w=w+(alpha*d)
    k += 1

if k == max_iter:
    print("El algoritmo no ha convergido.")

y = data.iloc[:, -1].values
y_pred_final = X @ w
y_pred_final = y_pred_final * y.std() + y.mean()

print("\nComparación de las 5 primeras viviendas:")
for i in range(5):
    print(f"Vivienda {i+1}: Real = {y[i]:.2f}, Predicho = {y_pred_final[i]:.2f}")