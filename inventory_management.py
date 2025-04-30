"""
Programa de gestión de inventario

Este programa permite gestionar un inventario de productos,
incluyendo agregar, buscar, actualizar precios, eliminar productos
y calcular el valor total del inventario.
"""


def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.
    :param inventario: Lista de diccionarios que representa el inventario.
    :param nombre: Nombre del producto.
    :param precio: Precio del producto.
    :param cantidad: Cantidad del producto.
    """
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' agregado al inventario.")
    return inventario


def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario por su nombre.
    :param inventario: Lista de diccionarios que representa el inventario.
    :param nombre: Nombre del producto a buscar.
    :return: Tupla nombre, precio y cantidad del producto, o None si no se encuentra.
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto["nombre"], producto["precio"], producto["cantidad"]
    print(f"Producto '{nombre}' no encontrado en el inventario.")
    return None


def actualizar_precio(inventario, nombre, nuevo_precio):
    """
    Actualiza el precio de un producto en el inventario.
    :param inventario: Lista de diccionarios que representa el inventario.
    :param nombre: Nombre del producto a actualizar.
    :param nuevo_precio: Nuevo precio del producto.
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["precio"] = nuevo_precio
            print(f"Precio del producto '{nombre}' actualizado a {nuevo_precio}.")
            return
    print(f"Producto '{nombre}' no encontrado en el inventario.")


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    :param inventario: Lista de diccionarios que representa el inventario.
    :param nombre: Nombre del producto a eliminar.
    """
    for i, producto in enumerate(inventario):
        if producto["nombre"].lower() == nombre.lower():
            del inventario[i]
            print(f"Producto '{nombre}' eliminado del inventario.")
            return
    print(f"Producto '{nombre}' no encontrado en el inventario.")


def calcular_valor_total(inventario):
    """
    Calcula el valor total del inventario con una lambda.
    :param inventario: Lista de diccionarios que representa el inventario.
    :return: Valor total del inventario.
    """
    valor_total = sum(map(lambda x: x["precio"] * x["cantidad"], inventario))
    return valor_total


def mostrar_inventario(inventario):
    """
    Muestra el inventario de productos.
    :param inventario: Lista de diccionarios que representa el inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario:")
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")


# Menú de opciones
def menu():
    while True:
        print("\n---------- Menú de opciones ----------")
        print("Seleccione una opción:")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar inventario")
        print("7. Salir")
        print("--------------------------------------")

        opcion = input("Ingrese su opción: ")
        return opcion


# Programa principal
print("---------- Bienvenido al programa de gestión de inventario ----------")

inventario = []  # Lista para almacenar los productos

while True:
    try:
        opcion = menu()
        match opcion:
            case '1':
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                inventario = agregar_producto(inventario, nombre, precio, cantidad)

            case '2':
                nombre = input("Ingrese el nombre del producto a buscar: ")
                resultado = buscar_producto(inventario, nombre)
                if resultado:
                    print(
                        f"Producto encontrado - Nombre: {resultado[0]}, Precio: {resultado[1]}, Cantidad: {resultado[2]}")

            case '3':
                nombre = input("Ingrese el nombre del producto a actualizar: ")
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                actualizar_precio(inventario, nombre, nuevo_precio)

            case '4':
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                eliminar_producto(inventario, nombre)

            case '5':
                valor_total = calcular_valor_total(inventario)
                print(f"Valor total del inventario: {valor_total}")

            case '6':
                mostrar_inventario(inventario)

            case '7':
                print("Saliendo del programa...")
                print("--------------------------------------")
                break

            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
    except ValueError as e:
        print(f"Error de entrada: {e}. Por favor, ingrese datos válidos.")
