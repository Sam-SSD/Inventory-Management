import inventory
import utils

# Main inventory instance
inventory = inventory.Inventory()
inventory.add_products("Apple", 1.00, 10)
inventory.add_products("Banana", 0.50, 15)
inventory.add_products("Orange", 0.75, 12)
inventory.add_products("Milk", 2.50, 8)
inventory.add_products("Bread", 1.25, 20)


def handle_add_product():
    """
    Manages the logic for adding a new product to inventory.
    Requests the name, price, and quantity from the user.
    """
    print("\n------------------ Add Product ------------------")
    name = utils.validate_name("Enter the name of the product: ")
    price = utils.validate_price("Enter the price of the product: ")
    quantity = utils.validate_quantity("Enter the quantity: ")
    inventory.add_products(name, price, quantity)
    print("------------------------------------------------------")


def handle_search_product():
    """
    Manages the search for a product by name and displays the information if it is found.
    """
    print("\n------------------ Search Product -------------------")
    if utils.validate_available_product(inventory):
        name = utils.validate_name("Enter the name of the product to search: ")
        product = inventory.search_product(name)
        if product:
            print(
                f"🔎 Product Found: {product['name']} | Price: ${product['price']:,.2f} | Quantity: {product['quantity']}")
        print("------------------------------------------------------")
    else:
        return


def handle_update_price():
    """
    Allows updating the price of an existing product.
    """
    print("\n---------------- Update Price -------------------")
    if utils.validate_available_product(inventory):
        name = utils.validate_name("Enter the name of the product to update: ")
        new_price = utils.validate_price("Enter the new price: ")
        inventory.update_price(name, new_price)
        print("------------------------------------------------------")
    else:
        return


def handle_delete_product():
    """
    Allows removing a product from the inventory if it exists.
    """
    print("\n---------------- Delete Product -------------------")
    if utils.validate_available_product(inventory):
        name = utils.validate_name("Enter the name of the product to delete: ")
        inventory.delete_product(name)
    else:
        return


def handle_total_value():
    """
    Calculates and displays the total value of the inventory.
    """
    print("\n------------ Total Value of Inventory -------------")
    if utils.validate_available_product(inventory):
        total = inventory.calculate_total_value()
        print(f"💰 Total inventory value: ${total:,.2f}")
        print("-----------------------------------------------------")
    else:
        return


def handle_show_inventory():
    """
    Displays all products in the inventory in a readable list.
    """
    print("\n------------------ Show Inventory ----------------")
    inventory.show_inventory()
    print("------------------------------------------------------")


def menu():
    """
    Displays the main menu and returns the option selected by the user.

    Returns:
        str: Option chosen by the user.
    """
    print("\n📌 Options menu:")
    print("1. Add product")
    print("2. Search product")
    print("3. Update price")
    print("4. Delete product")
    print("5. Total value of inventory")
    print("6. Show inventory")
    print("7. Exit")
    return input("Select an option: ").strip()


# Start of program
print("\n🔧 Welcome to the inventory management system 🔧")
while True:
    try:
        option = menu()

        match option:
            case "1":
                handle_add_product()
            case "2":
                handle_search_product()
            case "3":
                handle_update_price()
            case "4":
                handle_delete_product()
            case "5":
                handle_total_value()
            case "6":
                handle_show_inventory()
            case "7":
                print("\n👋 Exiting the program. ¡See you later!")
                print("------------------------------------------------------")
                break
            case _:
                print("\n❗ Invalid option. Please try again.")
                print("------------------------------------------------------")

    except Exception as error:
        print(f"\n Error: {error}.")
        print("------------------------------------------------------")
