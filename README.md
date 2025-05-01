![Inventory management system](https://github.com/user-attachments/assets/f853b6a5-15d5-45a8-8c47-8f1721fa6ed5)

# 🧾 Sistema de Gestión de Inventario

### 📘 English version  
[Click here to see the README in English](./README_EN.md)


## 📌 Descripción del Proyecto

Este proyecto forma parte del **Módulo 1 – Semana 3 del entrenamiento en desarrollo de software**, enfocado en aplicar **funciones con parámetros, valores de retorno, funciones lambda y colecciones de datos en Python**. El objetivo principal es diseñar un sistema interactivo para gestionar el inventario de una tienda, utilizando listas y diccionarios para controlar eficientemente los productos.

---

## 🎯 Funcionalidades

- **Agregar productos**: Cada producto incluye nombre, precio y cantidad disponible.
- **Buscar productos** por nombre: Retorna precio y cantidad si se encuentra.
- **Actualizar precios** de productos de forma interactiva.
- **Eliminar productos** del inventario.
- **Calcular el valor total del inventario** utilizando una función lambda.
- **Mostrar el inventario completo** de manera clara y legible.

---

## 🧠 Lógica Implementada

- Se emplearon **funciones con parámetros y retornos** para modularizar el programa.
- Se utilizó una **función lambda** para calcular el valor total del inventario.
- **Estructuras de control**: `match-case`, `try-except`, bucles y validaciones para la entrada del usuario.
- Los productos se almacenan en una **lista de diccionarios**, permitiendo un crecimiento dinámico del inventario.

---

## ✅ Validaciones Realizadas

- Validación de entradas para evitar errores (por ejemplo, precio y cantidad deben ser numéricos).
- Búsqueda y coincidencias no sensibles a mayúsculas/minúsculas.
- Eliminación y actualización seguras de productos.
- Casos límite probados:
  1. Búsqueda de productos inexistentes
  2. Ingreso de nombres duplicados
  3. Tipos de datos inválidos
  4. Inventario vacío

---

## 📁 Estructura del Código

- `agregar_producto`: Agrega un nuevo producto al inventario.
- `buscar_producto`: Busca por nombre y retorna la información del producto.
- `actualizar_precio`: Actualiza el precio de un producto dado.
- `eliminar_producto`: Elimina un producto de forma segura.
- `calcular_valor_total`: Utiliza una lambda para calcular el valor total.
- `mostrar_inventario`: Muestra todos los productos en una lista formateada.
- `menu`: Menú interactivo en consola para navegar entre funciones.

---

## 💡 Justificación Técnica

- Se optó por una **lista de diccionarios** por su flexibilidad y claridad estructural.
- Las funciones modulares favorecen la **legibilidad, mantenimiento y escalabilidad**.
- La función lambda se integró eficientemente para el cálculo rápido del inventario.
- El uso de `match-case` mejora la fluidez del menú y `try-except` ofrece mejor experiencia de usuario.

---

## 🚀 Posibles Mejoras Futuras

- Guardar/cargar el inventario desde archivos externos (CSV o JSON).
- Evitar nombres de productos duplicados.
- Añadir categorías o etiquetas a los productos.
- Incluir opciones de ordenamiento y filtrado.
- Construir una interfaz gráfica con Tkinter o PyQt.

---

## 💻 Instrucciones de Ejecución

1. Asegúrate de tener Python 3.8 o superior instalado.
2. Clona este repositorio desde GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Inventory-Management.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd Inventory-Management
   ```

4. Ejecuta el archivo principal:

   ```bash
   python inventory_management.py
   ```

5. Usa el menú interactivo para agregar, buscar, actualizar o eliminar productos.

---
