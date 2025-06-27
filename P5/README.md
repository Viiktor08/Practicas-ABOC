# Práctica 5: Redes de Hopfield — El Problema de las N-Torres

Este repositorio contiene la implementación de una **Red de Hopfield** para resolver el problema de colocar **N torres** en un tablero de ajedrez N×N sin que se ataquen entre sí. La red se configura para minimizar una función de energía que penaliza los conflictos en filas y columnas.

## 📌 Descripción

El problema de las N-Torres es una variante del problema de las N-Reinas. Cada torre se puede mover en línea recta por filas y columnas, por lo tanto, dos torres no pueden compartir fila ni columna.

La Red de Hopfield se usa aquí como un sistema de optimización, donde:

- Cada celda del tablero es una neurona binaria (1 = torre, 0 = vacío).
- La energía del sistema se define para penalizar conflictos.
- La red evoluciona dinámicamente hasta alcanzar un mínimo de energía, que representa una solución válida.

## 📁 Estructura del Proyecto

```
├── Hopfield_NTorres.py            # Implementación de la red de Hopfield para el problema de las torres
```

## ⚙️ Requisitos

- Python 3.x
- Librerías:
  - numpy
  - matplotlib (opcional, si se visualiza el tablero)

Instalación de dependencias:
```bash
pip install numpy matplotlib
```

## 🧪 Instrucciones de Ejecución

1. Ejecutar el script:
```bash
python Hopfield_NTorres.py
```
2. El script configurará la red, la hará evolucionar y mostrará el estado final del tablero.

## 🧠 Lógica Implementada

- **Función de energía**: Penaliza más de una torre en la misma fila o columna.
- **Pesos sinápticos**: Configurados para reflejar estas restricciones.
- **Dinámica de actualización**: La red evoluciona hasta que la energía se estabiliza.

## 🎯 Objetivo Académico

- Aplicar redes neuronales recurrentes a problemas combinatorios.
- Comprender el comportamiento de las redes de Hopfield como sistemas dinámicos.
- Desarrollar habilidades de modelado energético en sistemas complejos.

## 👤 Autor

- Víctor Tirado  
- victortiradoarregui@uma.es  
- Universidad de Málaga — Algoritmos de Búsqueda y Optimización Computacional

## 📄 Licencia

Este proyecto es solo con fines académicos.
