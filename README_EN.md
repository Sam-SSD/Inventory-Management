
![Inventory management system](https://github.com/user-attachments/assets/f853b6a5-15d5-45a8-8c47-8f1721fa6ed5)

# 🧾 Inventory Management System

### 📘 Versión en español  
[Haz clic aquí para ver el README en español](./README.md)

---

## 📌 Project Description

This project is part of **Module 1 – Week 3 of the software development training**, aiming to build a modular, reusable, and scalable inventory management system. The new version is implemented in **Python using object-oriented programming (OOP)**, distributing logic across classes and independent files to improve maintainability and code clarity.

---

## 🎯 Features

- **Add products** with name, price, and available quantity. Duplicate product names are not allowed.
- **Search products** by name and display detailed information.
- **Update prices** of existing products.
- **Delete products** from the inventory by name.
- **Calculate total inventory value** automatically.
- **Display the entire inventory** in a clear, readable format with thousands separators.

---

## 🧠 Implemented Logic

- A class named `Inventario` encapsulates all business logic.
- Input validations are abstracted into a separate `utils.py` file.
- The interactive menu and program flow are handled from `main.py`.
- The `match-case` structure (Python 3.10+) is used to manage the menu logic.
- Products are stored in a list of dictionaries, allowing dynamic growth.

---

## ✅ Validations Implemented

- Strict input validation to prevent errors:
  - Name must be non-empty and non-numeric.
  - Name must be unique (no duplicates allowed).
  - Price must be a positive decimal number.
  - Quantity must be a positive integer.
- Case-insensitive product name comparisons.
- Prices and totals use thousands separators.
- Exception handling with `try-except` for unexpected input errors.
- Considered scenarios:
  1. Empty inventory
  2. Non-existent products
  3. Duplicate product names
  4. Invalid data types
  5. Repeated or redundant operations

---

## 📁 Project Structure

```
inventory_app/
├── main.py           # Interactive menu and application logic
├── inventory.py      # Inventario class containing all core methods
└── utils.py          # Helper functions for user input validation
```

---

## 🧩 File Descriptions

- `main.py`: Manages the system's execution flow and user interaction.
- `inventory.py`: Contains the `Inventario` class, which handles product addition, search, updates, deletions, and total calculation.
- `utils.py`: Includes reusable functions to validate user input: name, price, and quantity.

---

## 💡 Technical Justification

- Object-oriented design improves **modularity** and enables future expansion.
- File separation enhances **code organization and reuse**.
- A clear text-based interface provides intuitive interaction and user feedback.
- Good practices were applied: encapsulation, inline documentation, and error handling.

---

## 🚀 Possible Future Improvements

- Add product categories and tags.
- Export/import inventory from/to CSV or JSON files.
- Implement custom filters and sorting options.
- Build a GUI with Tkinter, PyQt, or a web interface using Flask.

---

## 💻 Execution Instructions

1. Make sure Python 3.10 or higher is installed.
2. Clone this repository from GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Inventory-Management.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Inventory-Management
   ```

4. Navigate into the app folder:

   ```bash
   cd inventory_app
   ```

5. Run the main script:

   ```bash
   python main.py
   ```

6. Use the menu to manage your store's inventory.

---
