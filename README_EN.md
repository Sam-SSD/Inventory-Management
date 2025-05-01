![Inventory management system](https://github.com/user-attachments/assets/f853b6a5-15d5-45a8-8c47-8f1721fa6ed5)

# 🧾 Inventory Management System

## 📌 Project Description

This project is part of the **Module 1 – Week 3 of the software development training**, focused on applying **functions with parameters, return values, lambda functions, and data collections in Python**. The main goal is to design an interactive inventory management system for a store, allowing efficient control over products using lists and dictionaries.

---

## 🎯 Features

- **Add products**: Each product includes a name, price, and available quantity.
- **Search for products** by name: Returns price and quantity if found.
- **Update product prices** interactively.
- **Delete products** from the inventory.
- **Calculate total inventory value** using a lambda function.
- **Display full inventory** in a readable format.

---

## 🧠 Logic Implemented

- **Functions with parameters and return values** were used to modularize the program.
- **Lambda function** is used to compute the total inventory value.
- **Control structures**: `match-case`, `try-except`, loops, and validations for user input.
- Products are stored in a **list of dictionaries**, enabling dynamic inventory growth.

---

## ✅ Validations Performed

- Data input is validated to avoid crashes (e.g., price and quantity must be numeric).
- Case-insensitive search and matching.
- Safe deletion and updating mechanisms.
- Multiple edge cases tested:
  1. Searching for non-existent products
  2. Adding duplicate names
  3. Invalid data types in inputs
  4. Empty inventory cases

---

## 📁 Code Structure

- `agregar_producto`: Adds a new product to the inventory.
- `buscar_producto`: Searches by name and returns product info.
- `actualizar_precio`: Updates the price of a given product.
- `eliminar_producto`: Deletes a product safely.
- `calcular_valor_total`: Uses a lambda to compute inventory value.
- `mostrar_inventario`: Displays all products in a formatted list.
- `menu`: Interactive CLI menu for user navigation.

---

## 💡 Technical Justification

- The decision to use a list of dictionaries provides flexibility and clarity.
- Modular functions improve **readability**, **maintenance**, and **scalability**.
- The lambda function was effectively integrated for fast total value calculation.
- `match-case` improves flow readability, and `try-except` blocks improve UX.

---

## 🚀 Future Enhancements

- Save/load inventory from external files (CSV or JSON).
- Prevent duplicate product names.
- Add product categories or tags.
- Add sorting and filtering options.
- Build a GUI using Tkinter or PyQt.

---

## 💻 How to Run

1. Make sure you have Python 3.8+ installed.
2. Clone this repository from GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Inventory-Management.git
    ```
3. Navigate to the project directory:
    ```bash
    cd Inventory-Management
    ```
   
4. Run the main file:
    ```bash
    python inventory_management.py
    ```
   
5. Use the menu to add, search, update, or delete products.

---
