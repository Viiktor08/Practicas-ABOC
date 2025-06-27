# Práctica 4: Programación Entera — La Rejilla Mágica

Este repositorio contiene una implementación del puzzle conocido como **Rejilla Mágica**, donde el objetivo es rellenar una cuadrícula N×N con enteros positivos bajo restricciones de suma en subrejillas. El problema ha sido modelado como un caso de **programación entera** y resuelto mediante la biblioteca **PuLP**.

## 📌 Descripción

Dado un tablero de dimensión N×N, se deben ubicar números enteros no negativos (≥ 0) en cada celda, de forma que:

- Toda subrejilla de tamaño **M×L** tenga suma **K**
- Toda subrejilla de tamaño **L×M** tenga también suma **K**

Se utiliza un solver de programación entera para obtener una rejilla que satisfaga las restricciones.

## 📁 Estructura del Proyecto

```
├── RejillaMagica.py                  # Script principal con el modelo de optimización
```

## ⚙️ Requisitos

- Python 3.x
- Librerías:
  - numpy
  - PuLP

Instalación de dependencias:
```bash
pip install numpy pulp
```

## 🧪 Instrucciones de Ejecución

1. Ejecuta el script indicando valores para N, M, L, K dentro del código o mediante entrada estándar.
2. El script modela el problema y muestra por consola la rejilla resultante.
```bash
python RejillaMagica.py
```

## 🎯 Objetivo Académico

- Modelar restricciones combinatorias mediante programación entera.
- Utilizar subrejillas como unidad de control para validar soluciones.
- Aplicar herramientas como PuLP en problemas de estructura matricial.

## 👤 Autor

- Víctor Tirado  
- victortiradoarregui@uma.es  
- Universidad de Málaga — Algoritmos de Búsqueda y Optimización Computacional

## 📄 Licencia

Este proyecto es solo con fines académicos.
