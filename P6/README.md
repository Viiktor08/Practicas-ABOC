# Práctica 6: Metaheurísticas Poblacionales — Optimización de Carteras con CMA-ES

Este repositorio contiene la implementación de un algoritmo **CMA-ES modificado** (Covariance Matrix Adaptation Evolution Strategy) para resolver un problema de optimización de carteras bajo el modelo de **Markowitz con restricciones**.

## 📌 Descripción

Se ha trabajado con precios reales de 20 activos financieros extraídos del índice S&P100 para construir carteras que:

- Maximizan rentabilidad y minimizan riesgo (varianza).
- Cumplen con dos restricciones clave:
  - **Restricción de presupuesto**: la suma de pesos debe ser 1.
  - **Restricción de cardinalidad**: como máximo K activos pueden tener peso positivo.

El algoritmo evolutivo CMA-ES se ha adaptado mediante un operador de proyección para cumplir ambas restricciones durante la optimización.

## 📁 Estructura del Proyecto

```
├── cma_es_portafolio.py                 # Implementación del CMA-ES modificado con proyección
├── P6_ABOC.pdf                          # Informe completo con análisis de resultados
```

## ⚙️ Requisitos

- Python 3.x
- Librerías:
  - numpy
  - pandas
  - yfinance
  - matplotlib (opcional para visualizaciones)

Instalación de dependencias:
```bash
pip install numpy pandas yfinance matplotlib
```

## 🧪 Instrucciones de Ejecución

1. El script descarga automáticamente precios de activos vía `yfinance`.
2. Preprocesa los datos, calcula retornos, medias y covarianzas.
3. Lanza el algoritmo CMA-ES con operador de proyección.
4. Evalúa la cartera óptima sobre datos de validación.

```bash
python cma_es_portafolio.py
```

## 🔍 Detalles Técnicos

- Se utiliza proyección dura: se eliminan pesos negativos, se seleccionan los K más grandes y se normaliza.
- La función objetivo es:  
  `(1/2) * wᵀΣw - λ * wᵀμ`  
  donde `w` es el vector de pesos proyectado.
- Valores típicos: `K = 8`, `λ = 1, 10, 50`.

## 📊 Resultados

- Con λ = 10 y K = 8 se obtuvo una cartera con **sobreajuste a un único activo (NVDA)**.
- Evaluación fuera de muestra (enero-febrero 2025):
  - Rentabilidad diaria: −0.0028
  - Volatilidad: 0.0452
  - Sharpe ratio: −0.0610

## 📌 Conclusiones

- La **proyección dura** es simple pero puede empobrecer la diversidad.
- CMA-ES necesita mecanismos para fomentar diversidad y evitar convergencia a soluciones degeneradas.
- La elección de λ es clave para controlar el riesgo del inversor.

## 👤 Autor

- Víctor Tirado  
- victortiradoarregui@uma.es  
- Universidad de Málaga — Algoritmos de Búsqueda y Optimización Computacional

## 📄 Licencia

Este proyecto es solo con fines académicos.
