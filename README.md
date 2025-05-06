![Inventory management system](https://github.com/user-attachments/assets/f853b6a5-15d5-45a8-8c47-8f1721fa6ed5)

# 🧾 Sistema de Gestión de Inventario

### 📘 English version

[Click here to see the README in English](./README_EN.md)

---

## 📌 Descripción del Proyecto

Este proyecto forma parte del **Módulo 1 – Semana 3 del entrenamiento en desarrollo de software**, con el objetivo de
construir un sistema de gestión de inventario modular, reutilizable y escalable. La nueva versión está implementada en *
*Python con programación orientada a objetos (OOP)**, distribuyendo la lógica en clases y archivos independientes para
favorecer la mantenibilidad y claridad del código.

---

## 🎯 Funcionalidades

- **Agregar productos** con nombre, precio y cantidad disponibles. No permite productos con nombres duplicados.
- **Buscar productos** por nombre y mostrar su información detallada.
- **Actualizar precios** de productos ya existentes.
- **Eliminar productos** del inventario por nombre.
- **Calcular el valor total del inventario** de forma automatizada.
- **Mostrar el inventario completo** de manera clara y legible con separación de miles.

---

## 🧠 Lógica Implementada

- Se implementó una clase `Inventario` que encapsula toda la lógica de negocio.
- Las validaciones de entrada se abstrajeron en un archivo `utils.py`.
- El menú interactivo y el control del flujo se gestionan desde `main.py`.
- Se utilizó la estructura `match-case` (Python 3.10+) para organizar el menú.
- Se emplean listas de diccionarios como estructura para cada producto del inventario.

---

## ✅ Validaciones Realizadas

- Validación estricta para evitar errores de entrada:
    - Nombre no vacío ni numérico.
    - Nombre único (no duplicado).
    - Precio mayor que cero y en formato decimal.
    - Cantidad como número entero positivo.
- Búsquedas no sensibles a mayúsculas/minúsculas.
- Separadores de miles para precios y totales.
- Manejo de excepciones (`try-except`) para errores inesperados.
- Casos contemplados:
    1. Inventario vacío
    2. Productos inexistentes
    3. Nombres duplicados
    4. Tipos de datos inválidos
    5. Operaciones repetidas o redundantes

---

## 📁 Estructura del Proyecto

```
inventory_app/
├── main.py           # Menú interactivo y flujo del sistema
├── inventory.py      # Clase Inventario con todos los métodos del sistema
└── utils.py          # Funciones auxiliares para validación de datos
```

---

## 🧩 Descripción de Archivos

- `main.py`: Controla la ejecución principal del sistema. Contiene el menú y la interacción con el usuario.
- `inventory.py`: Contiene la clase `Inventario`, que permite agregar, buscar, actualizar, eliminar productos y calcular
  el valor total.
- `utils.py`: Incluye funciones reutilizables para validar entradas del usuario: nombre, precio y cantidad.

---

## 💡 Justificación Técnica

- Se utilizó orientación a objetos para mejorar la **modularidad** y facilitar futuras ampliaciones.
- La separación por archivos mejora la **organización y reutilización del código**.
- Se priorizó una **interfaz clara por consola**, con feedback útil para el usuario.
- Se aplicaron buenas prácticas: encapsulamiento, documentación interna y control de errores.

---

## 🚀 Posibles Mejoras Futuras

- Agregar categorías y etiquetas por producto.
- Exportar/importar inventario a archivos CSV o JSON.
- Implementar filtros y ordenamientos personalizados.
- Integrar una interfaz gráfica con Tkinter, PyQt o web (Flask).

---

## 💻 Instrucciones de Ejecución

1. Asegúrate de tener Python 3.10 o superior instalado.
2. Clona este repositorio desde GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Inventory-Management.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd Inventory-Management
   ```
4. Navega al directorio del proyecto:

   ```bash
   cd inventory_app
   ```

5. Ejecuta el sistema desde el archivo principal:

   ```bash
   python main.py
   ```

6. Interactúa con el menú para gestionar el inventario de tu tienda.

---
