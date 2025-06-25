import numpy as np
import pandas as pd
import yfinance as yf
import os
import certifi
import matplotlib.pyplot as plt
import cma

# Usar certificado SSL correcto
os.environ['SSL_CERT_FILE'] = certifi.where()


# PARTE I: CARGA DE DATOS


def descargar_datos(activos, inicio, fin):
    df = yf.download(activos, start=inicio, end=fin, progress=False)['Close']
    df = df.dropna(axis=1)  # Eliminar activos con datos faltantes
    return df

def calcular_rentabilidades(precios):
    return precios.pct_change().dropna()

def obtener_estadisticas(rentabilidades):
    mu = rentabilidades.mean().values
    sigma = rentabilidades.cov().values
    return mu, sigma


# PARTE II: PROYECCION DE PESOS


def proyectar_pesos(w, K):
    if w is None:
        raise RuntimeError("CMA-ES no devolvió una solución válida.")
    w = np.maximum(w, 0)
    idx = np.argsort(w)[-K:]
    w_filtrado = np.zeros_like(w)
    w_filtrado[idx] = w[idx]
    if w_filtrado.sum() > 0:
        w_filtrado /= w_filtrado.sum()
    return w_filtrado


# PARTE III: FUNCION OBJETIVO


def funcion_objetivo(w, mu, sigma, lam, K):
    w_proj = proyectar_pesos(w, K)
    varianza = 0.5 * w_proj.T @ sigma @ w_proj
    rendimiento = mu @ w_proj
    return varianza - lam * rendimiento


# PARTE IV: OPTIMIZACION CMA-ES


def optimizar(mu, sigma, lam=1.0, K=10):
    if np.any(np.isnan(mu)) or np.any(np.isnan(sigma)):
        raise ValueError("mu o sigma contiene NaNs. Verifica los datos de entrada.")
    S = len(mu)
    w0 = np.ones(S) / S
    es = cma.CMAEvolutionStrategy(w0, 0.2, {'maxiter': 100, 'verb_disp': 0})

    def f_cma(w):
        return funcion_objetivo(w, mu, sigma, lam, K)

    es.optimize(f_cma)
    return proyectar_pesos(es.result.xbest, K)


if __name__ == "__main__":
    activos = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'JPM', 'UNH', 'V', 'MA', 'HD', 'KO', 'PEP', 'DIS', 'INTC', 'ORCL', 'TSLA', 'IBM', 'CSCO', 'CVX' ]
    

    precios_2024 = descargar_datos(activos, '2024-01-01', '2024-12-31')
    rentabilidades_2024 = calcular_rentabilidades(precios_2024)
    mu, sigma = obtener_estadisticas(rentabilidades_2024)

    lam = 10
    K = 8
    
    try:
        w_opt = optimizar(mu, sigma, lam=lam, K=K)
    except Exception as e:
        print(f"Error en la optimización: {e}")
        exit()

    print("Pesos optimizados:")
    for activo, peso in zip(precios_2024.columns, w_opt):
        print(f"{activo}: {peso:.4f}")

    precios_2025 = descargar_datos(precios_2024.columns.tolist(), '2025-01-01', '2025-02-28')
    rentab_2025 = calcular_rentabilidades(precios_2025)

    if rentab_2025.empty:
        print("No se pudieron obtener rentabilidades de validación.")
        exit()

    cartera_2025 = rentab_2025 @ w_opt
    media_val = cartera_2025.mean()
    std_val = cartera_2025.std()
    sharpe_ratio = media_val / std_val if std_val > 0 else 0

    print("\nValidación en 2025:")
    print(f"Rentabilidad media: {media_val:.4f}")
    print(f"Volatilidad: {std_val:.4f}")
    print(f"Ratio de Sharpe: {sharpe_ratio:.4f}")
    plt.plot(np.cumprod(1 + cartera_2025.values) - 1)
    plt.title("Evolución de la cartera en validación (2025)")
    plt.xlabel("Días")
    plt.ylabel("Rentabilidad acumulada")
    plt.grid()
    plt.tight_layout()
    plt.show()
