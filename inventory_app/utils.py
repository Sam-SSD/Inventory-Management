def validate_name(message):
    """
    Prompts the user for a valid name.

    Requirements:
    - Must not be empty.
    - Must not be numeric.

    Parameters:
    message (str): Text to display as an instruction.

    Returns:
    str: Validated name.
    """
    while True:
        name = input(message).strip()
        if not name or name.isnumeric():
            print("❌ Invalid name. Please enter a valid name.")
        else:
            return name


def validate_price(message):
    """
    Prompts the user for a valid numeric price.

    Requirements:
    - Must be a float.
    - Must be greater than zero.

    Parameters:
    message (str): Text to display as an instruction.

    Returns:
    float: Validated price.
    """
    while True:
        try:
            price = float(input(message))
            if price <= 0:
                print("❌ The price must be greater than zero.")
            else:
                return price
        except ValueError:
            print("❌ Invalid entry. Please enter a valid number for the price.")


def validate_quantity(message):
    """
    Prompts the user for a valid integer quantity.

    Requirements:
    - Must be an integer.
    - Must be greater than zero.

    Parameters:
    message (str): Text to display as an instruction.

    Returns:
    int: Validated quantity.
    """
    while True:
        try:
            quantity = int(input(message))
            if quantity <= 0:
                print("❌ The quantity must be greater than zero.")
            else:
                return quantity
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")


def validate_available_product(inventory):
    """
    Validates if there are any available products in the inventory.
    If not, it informs the user and returns False.
    Otherwise, it returns True.
    Args:
        inventory (inventory): The inventory instance to check.
    Returns:
        bool: True if there are available books, False otherwise.
    """
    if not inventory.products:
        print("❌ No books available in the library.")
        print("------------------------------------------------")
        return False
    else:
        return True
