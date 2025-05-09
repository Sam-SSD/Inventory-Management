![Inventory management system](https://github.com/user-attachments/assets/f853b6a5-15d5-45a8-8c47-8f1721fa6ed5)

# 🧾 Sistema de Gestión de Inventario

### 📘 English version

[Click here to see the README in English](./README_EN.md)

---

## 📌 Descripción del Proyecto

Este proyecto hace parte del **Módulo 1 – Semana 3 del entrenamiento en desarrollo de software**, y tiene como objetivo construir un **sistema interactivo de gestión de inventario** usando **Python**. Esta versión está diseñada bajo principios de **modularidad y separación de responsabilidades**, con lógica dividida en archivos independientes (`main.py`, `inventory.py`, `utils.py`) para mejorar la escalabilidad, el mantenimiento y la legibilidad del código.

---

## 🎯 Funcionalidades

- **Agregar productos** con nombre, precio y cantidad disponible (no se permiten nombres duplicados).
- **Buscar productos** por nombre.
- **Actualizar el precio** de productos existentes.
- **Eliminar productos** del inventario.
- **Calcular el valor total del inventario** con separación de miles y una operación lambda.
- **Mostrar el inventario completo** con una presentación clara y organizada.

---

## 🧠 Lógica Implementada

- Uso de una clase `Inventario` que encapsula toda la lógica del sistema.
- Separación del código en módulos:
  - `main.py` gestiona la interfaz de usuario y el flujo general.
  - `inventory.py` contiene toda la lógica de negocio.
  - `utils.py` centraliza las validaciones de entrada.
- Se usa `match-case` (Python 3.10+) para el control de flujo del menú.
- Todas las funcionalidades están implementadas como funciones separadas (`manejar_*`) para facilitar la legibilidad y el mantenimiento.

---

## ✅ Validaciones Realizadas

- Validaciones robustas para evitar entradas inválidas:
  - **Nombre**: no vacío y no numérico.
  - **Precio**: numérico, mayor que cero.
  - **Cantidad**: entero positivo.
- Búsqueda no sensible a mayúsculas/minúsculas.
- Se evita el ingreso de nombres duplicados.
- Visualización con separadores de miles para montos monetarios.
- Control de errores global mediante bloques `try-except`.

---

## 📁 Estructura del Proyecto

```
inventory_app/
├── main.py         # Menú interactivo y control general del flujo
├── inventory.py    # Clase Inventario con toda la lógica de negocio
└── utils.py        # Validación modular de entradas del usuario
```

---

## 🧩 Descripción de Archivos

- **`main.py`**  
  Contiene las funciones del menú (`manejar_agregar_producto`, `manejar_buscar_producto`, etc.) y la ejecución principal del programa.

- **`inventory.py`**  
  Define la clase `Inventario`, que permite gestionar productos (agregar, buscar, actualizar, eliminar, mostrar e inventariar).

- **`utils.py`**  
  Proporciona funciones para validar entradas del usuario: nombre (str), precio (float) y cantidad (int), de forma reutilizable.

---

## 💡 Justificación Técnica

- La **modularidad** facilita las pruebas y futuras expansiones.
- La **orientación a funciones** y separación por archivo evita redundancia.
- Uso de **estilo profesional en comentarios y docstrings**, útil para desarrolladores nuevos en el proyecto.
- El código está preparado para integrarse en sistemas mayores o con interfaces gráficas.

---

## 🚀 Posibles Mejoras Futuras

- Clasificación de productos por categorías o etiquetas.
- Exportación e importación de inventario (CSV, JSON).
- Filtrado y ordenamiento de productos por precio, cantidad, etc.
- Interfaz gráfica usando Tkinter, PyQt o integración web con Flask o Django.

---

## 💻 Instrucciones de Ejecución

1. Asegúrate de tener **Python 3.10 o superior** instalado.
2. Clona este repositorio desde GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Inventory-Management.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd Inventory-Management/inventory_app
   ```

4. Ejecuta el sistema desde el archivo principal:

   ```bash
   python main.py
   ```

5. Usa el menú interactivo para agregar, buscar, actualizar o eliminar productos.

---