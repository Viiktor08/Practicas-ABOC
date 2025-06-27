# Práctica 3: Programación Entera — Problema del Viajante de Comercio (TSP)

Este repositorio contiene la implementación de una solución al clásico **Problema del Viajante de Comercio (TSP)** mediante técnicas de **programación entera** utilizando la biblioteca **PuLP** en Python. El objetivo es encontrar la ruta óptima que minimiza la distancia total recorrida por un vendedor que debe visitar un conjunto de ciudades exactamente una vez y regresar al punto de origen.

## 📌 Descripción

La práctica modela el TSP como un problema de optimización combinatoria:

- Se utiliza un conjunto de puntos generados aleatoriamente dentro de las fronteras de Estados Unidos.
- Se implementa un modelo de programación entera con:
  - Variables binarias para la toma de decisiones.
  - Función objetivo basada en la distancia total.
  - Restricciones de conectividad y subtours.

## 📁 Estructura del Proyecto

```
├── TSP-base.py         # Código base con secciones de generación, optimización y visualización
├── usborder.mat        # Archivo con las fronteras geográficas de Estados Unidos
```

## ⚙️ Requisitos

- Python 3.x
- Librerías:
  - numpy
  - scipy
  - matplotlib
  - PuLP
  - scipy.io (para leer archivos .mat)

Instalación de dependencias:
```bash
pip install numpy scipy matplotlib pulp
```

## 🧪 Instrucciones de Ejecución

1. Abre el archivo `TSP-base.py`.
2. Asegúrate de haber completado la sección de optimización si aún no lo has hecho.
3. Ejecuta el script:
```bash
python TSP-base.py
```
4. Se mostrará en pantalla la ruta óptima sobre el mapa de EE.UU. con las ciudades conectadas en el orden más eficiente.

## 🎯 Objetivo Académico

- Entender la formulación matemática del TSP.
- Aplicar programación entera para resolver un problema NP-hard.
- Utilizar herramientas como PuLP para modelado y resolución de problemas de optimización.

## 👤 Autor

- Víctor Tirado  
- victortiradoarregui@uma.es  
- Universidad de Málaga — Algoritmos de Búsqueda y Optimización Computacional

## 📄 Licencia

Este proyecto es solo con fines académicos.
