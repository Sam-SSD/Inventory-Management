class Inventory:
    def __init__(self):
        self.products = []

    def add_products(self, name, price, quantity):
        """
        Adds a new product to the inventory if there is no duplicate name (case-insensitive).

        Parameters:
            name (str): Product name.
            price (float): Unit price.
            quantity (int): Quantity available.
        """

        for p in self.products:
            if p["name"].lower() == name.lower():
                print(f"️⚠️ A product with the name '{name}' already exists. It has not been added.")
                return

        self.products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        print(f"✅ Product '{name}' added successfully.")

    def search_product(self, name):
        """
        Search for a product in the inventory by name (case-insensitive).

        Parameters:
            name (str): Name of the product to search for.

        Returns:
            dict: The product if found, or None if it doesn't exist.
        """
        for product in self.products:
            if product["name"].lower() == name.lower():
                return product
        print(f"❌ Product '{name}' not found.")
        return None

    def update_price(self, name, new_price):
        """
        Updates a product's price if it exists.

        Parameters:
            name (str): Product name.
            new_price (float): New price to assign.
        """
        product = self.search_product(name)
        if product:
            product["price"] = new_price
            print(f"🛠 Price of '{name}' updated to ${new_price:,.2f}.")

    def delete_product(self, name):
        """
        Deletes a product from inventory if it exists.

        Parameters:
            name (str): Name of the product to delete.
        """
        for i, product in enumerate(self.products):
            if product["name"].lower() == name.lower():
                del self.products[i]
                print(f"🗑 Product '{name}' deleted.")
                return
        print(f"❌ Product '{name}' not found.")

    def calculate_total_value(self):
        """
        Calculates the total inventory value using a lambda function.

        Returns:
            float: Total inventory value.
        """
        return sum(map(lambda p: p["price"] * p["quantity"], self.products))

    def show_inventory(self):
        """
        Displays all products in inventory with their price and available quantity.

        Returns:
            All products in inventory
        """
        if not self.products:
            print("📦 The inventory is empty")
        else:
            print("\n Current inventory:")
            for product in self.products:
                print(f"- {product['name']} | Price: ${product['price']:,.2f} | Quantity: {product['quantity']}")
