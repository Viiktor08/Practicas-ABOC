# Práctica 2: Optimización con Restricciones (ADALINA LASSO)

Este repositorio contiene la implementación de **ADALINA con regularización ℓ1 (LASSO)** para resolver un problema de regresión lineal. El modelo fue optimizado utilizando el **método de Gradiente Proyectado**, el cual impone restricciones sobre la norma ℓ1 del vector de pesos para fomentar la selección automática de características y evitar el sobreajuste.

## 📌 Descripción

Se ha trabajado sobre el mismo conjunto de datos que en la Práctica 1 (**Boston Housing**), aplicando regularización ℓ1. Se implementó el algoritmo de **Gradiente Proyectado** que realiza:

- Minimización de la función de pérdida regularizada:  
  min_{w} (1/2) * ||Xw - y||^2 + λ * ||w||_1
- Proyección del gradiente en el conjunto factible para respetar la restricción ℓ1.
- Selección dinámica del tamaño de paso mediante backtracking.

## 📁 Estructura del Proyecto

```
├── ADALINALassoGradienteProyectado.py # Implementación del Gradiente Proyectado con LASSO
├── hou_all.csv                        # Dataset de viviendas (Boston Housing)
├── P2_ABOC.pdf                        # Informe con resultados y análisis
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

1. El dataset `hou_all.csv` es cargado y preprocesado dentro del script (eliminación del bias y normalización).
2. El valor de **λ** usado por defecto es **100**.
3. Ejecutar el script:
```bash
python ADALINALassoGradienteProyectado.py
```

## 📊 Resultados

- Número de iteraciones hasta convergencia (λ = 100): **14**
- Algunos coeficientes se anulan completamente → se logra **sparsity**
- Comparación de los valores reales y predichos:

| Vivienda | Real | Predicho |
|----------|------|----------|
| 1        | 24.0 | 26.19    |
| 2        | 21.6 | 26.18    |
| 3        | 34.7 | 31.09    |
| 4        | 33.4 | 28.72    |
| 5        | 36.2 | 27.34    |

### 🔍 Análisis del efecto de λ

| λ       | Descripción                                         |
|---------|-----------------------------------------------------|
| 10      | Poca penalización, muchos coeficientes ≠ 0          |
| 50      | Aparecen ceros, mejora generalización               |
| 100     | Buen equilibrio entre ajuste y simplicidad          |
| 200     | Modelo muy penalizado, riesgo de **subajuste**      |

> Se muestra una gráfica en el informe del número de características seleccionadas según λ.

## 🧠 Conclusiones

- El **Gradiente Proyectado** permite abordar eficazmente problemas con restricciones ℓ1.
- La regularización LASSO introduce **sparsity**, lo que ayuda a seleccionar automáticamente características relevantes.
- La elección de **λ** es crítica para equilibrar **precisión** y **complejidad** del modelo.

## 👤 Autor

- Víctor Tirado  
- victortiradoarregui@uma.es  
- Universidad de Málaga — Algoritmos de Búsqueda y Optimización Computacional

## 📄 Licencia

Este proyecto es solo con fines académicos.
