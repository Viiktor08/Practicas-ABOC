# Práctica 1: Optimización sin Restricciones (ADALINA)

Este repositorio contiene la implementación del modelo **ADALINA (Adaptive Linear Neuron)** como solución a un problema de regresión lineal mediante dos métodos de optimización: **Descenso de Gradiente** y **Método de Newton**.

## 📌 Descripción

El objetivo de esta práctica es minimizar el error cuadrático entre las predicciones de ADALINA y los valores reales del conjunto de datos **Boston Housing**. Se ha realizado:

- Preprocesamiento del dataset.
- Implementación de ADALINA con:
  - Descenso de Gradiente (con cálculo exacto del paso óptimo).
  - Método de Newton (utilizando gradiente y matriz Hessiana).
- Comparación de ambos métodos en cuanto a iteraciones y precisión.

## 📁 Estructura del Proyecto

```
├── ADALINAGradiente.py         # Implementación con Descenso de Gradiente
├── ADALINANewton.py            # Implementación con Método de Newton
├── hou_all.csv                 # Dataset de viviendas (Boston Housing)
├── P1_ABOC.pdf                 # Informe con resultados y conclusiones
```

## ⚙️ Requisitos

- Python 3.x
- Librerías:
  - numpy
  - pandas

Instalación de dependencias:
```bash
pip install numpy pandas
```

## 🧪 Instrucciones de Ejecución

1. **Preprocesamiento**: el dataset `hou_all.csv` es cargado y normalizado internamente por ambos scripts.
2. **Ejecución**:
   - Para el descenso de gradiente:
     ```bash
     python ADALINAGradiente.py
     ```
   - Para el método de Newton:
     ```bash
     python ADALINANewton.py
     ```

## 📊 Resultados

Según el informe:

| Método               | Iteraciones hasta convergencia |
|----------------------|-------------------------------|
| Descenso de Gradiente| 320                           |
| Método de Newton     | 1                             |

Ambos métodos producen predicciones similares, pero el Método de Newton converge mucho más rápido debido al uso de derivadas de segundo orden.

## 🧠 Conclusiones

- El **Descenso de Gradiente** es más sencillo y computacionalmente barato, pero converge lentamente.
- El **Método de Newton** es más eficiente en términos de iteraciones gracias a su convergencia cuadrática, aunque requiere mayor capacidad computacional por el cálculo de la matriz Hessiana.

## 👤 Autor

- Víctor Tirado  
- victortiradoarregui@uma.es  
- Universidad de Málaga — Algoritmos de Búsqueda y Optimización Computacional

## 📄 Licencia

Este proyecto es solo con fines académicos.
