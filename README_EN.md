
![Inventory management system](https://github.com/user-attachments/assets/f853b6a5-15d5-45a8-8c47-8f1721fa6ed5)

# 🧾 Inventory Management System

### 📘 Versión en español  
[Haz clic aquí para ver el README en español](./README.md)

---

## 📌 Project Description

This project is part of **Module 1 – Week 3 of the software development training**, and its goal is to build an **interactive inventory management system** using **Python**. The current version is based on **modular design** and clear separation of concerns, distributing the logic across independent files (`main.py`, `inventory.py`, `utils.py`) to improve scalability, maintainability, and code clarity.

---

## 🎯 Features

- **Add products** with name, price, and quantity (duplicate names are not allowed).
- **Search products** by name.
- **Update prices** of existing products.
- **Delete products** from the inventory.
- **Calculate the total inventory value** with thousand separators and a lambda operation.
- **Display the entire inventory** in a clear and formatted view.

---

## 🧠 Implemented Logic

- A class called `Inventory` encapsulates all core business logic.
- Code is divided into modules:
  - `main.py` manages user interaction and the control flow.
  - `inventory.py` contains the inventory business logic.
  - `utils.py` centralizes input validation functions.
- Uses `match-case` (Python 3.10+) for the main menu.
- All menu actions are implemented as separate handler functions (`handle_*`) for clarity and maintainability.

---

## ✅ Input Validations

- Strict validation to prevent invalid entries:
  - **Name** must be non-empty and non-numeric.
  - **Name** must be unique (no duplicates).
  - **Price** must be a positive decimal number.
  - **Quantity** must be a positive integer.
- Case-insensitive name comparisons.
- Thousand separators used for monetary values.
- Exception handling using `try-except` blocks for robustness.

---

## 📁 Project Structure

```
inventory_app/
├── main.py         # Interactive menu and main application logic
├── inventory.py    # Inventory class with core business logic
└── utils.py        # Reusable validation functions for user input
```

---

## 🧩 File Descriptions

- **`main.py`**  
  Contains the program's entry point and functions like `handle_add_product`, `handle_search_product`, etc., to drive the user interaction.

- **`inventory.py`**  
  Defines the `Inventory` class which includes logic for adding, searching, updating, deleting, and displaying products.

- **`utils.py`**  
  Offers helper functions to validate user inputs such as name, price, and quantity.

---

## 💡 Technical Justification

- Object-oriented programming improves **modularity** and makes future enhancements easier.
- File separation promotes **clean organization and reuse**.
- The console interface provides a user-friendly experience with clear feedback.
- Professional practices were applied: encapsulation, modularity, inline documentation, and structured exception handling.

---

## 🚀 Possible Future Improvements

- Add product categories and custom tags.
- Export/import inventory to/from CSV or JSON files.
- Implement sorting and filtering by price, quantity, etc.
- Develop a graphical user interface with Tkinter, PyQt, or a web app using Flask or Django.

---

## 💻 Execution Instructions

1. Make sure you have **Python 3.10 or higher** installed.
2. Clone this repository from GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Inventory-Management.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Inventory-Management/inventory_app
   ```

4. Run the system from the main script:

   ```bash
   python main.py
   ```

5. Use the interactive menu to manage your store's inventory.

---