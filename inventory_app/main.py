from inventory import Inventario
import utils

# Instancia principal del inventario
inventario = Inventario()


def handle_agregar_producto():
    """
    Gestiona la lógica para agregar un nuevo producto al inventario.
    Solicita el nombre, precio y cantidad al usuario.
    """
    print("\n------------------ Agregar Producto ------------------")
    nombre = utils.validar_nombre("Ingrese el nombre del producto: ")
    precio = utils.validar_precio("Ingrese el precio del producto: ")
    cantidad = utils.validar_cantidad("Ingrese la cantidad: ")
    inventario.agregar_producto(nombre, precio, cantidad)
    print("------------------------------------------------------")


def handle_buscar_producto():
    """
    Gestiona la búsqueda de un producto por su nombre y muestra la información si lo encuentra.
    """
    print("\n------------------ Buscar Producto -------------------")
    nombre = utils.validar_nombre("Ingrese el nombre del producto a buscar: ")
    producto = inventario.buscar_producto(nombre)
    if producto:
        print(
            f"🔎 Encontrado: {producto['nombre']} | Precio: ${producto['precio']:,.2f} | Cantidad: {producto['cantidad']}")
    print("------------------------------------------------------")


def handle_actualizar_precio():
    """
    Permite actualizar el precio de un producto existente.
    """
    print("\n---------------- Actualizar Precio -------------------")
    nombre = utils.validar_nombre("Ingrese el nombre del producto a actualizar: ")
    nuevo_precio = utils.validar_precio("Ingrese el nuevo precio: ")
    inventario.actualizar_precio(nombre, nuevo_precio)
    print("------------------------------------------------------")


def handle_eliminar_producto():
    """
    Permite eliminar un producto del inventario si existe.
    """
    print("\n---------------- Eliminar Producto -------------------")
    nombre = utils.validar_nombre("Ingrese el nombre del producto a eliminar: ")
    inventario.eliminar_producto(nombre)
    print("------------------------------------------------------")


def handle_valor_total():
    """
    Calcula y muestra el valor total del inventario.
    """
    print("\n------------ Valor Total del Inventario -------------")
    total = inventario.calcular_valor_total()
    print(f"💰 Valor total del inventario: ${total:,.2f}")
    print("------------------------------------------------------")


def handle_mostrar_inventario():
    """
    Muestra todos los productos del inventario en una lista legible.
    """
    print("\n------------------ Mostrar Inventario ----------------")
    inventario.mostrar_inventario()
    print("------------------------------------------------------")


def menu():
    """
    Muestra el menú principal y devuelve la opción seleccionada por el usuario.

    Returns:
        str: Opción elegida por el usuario.
    """
    print("\n📌 Menú de opciones:")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar inventario")
    print("7. Salir")
    return input("Seleccione una opción: ").strip()


# --------------------- Inicio del Programa ---------------------
print("🔧 Bienvenido al sistema de gestión de inventario 🔧")

while True:
    try:
        opcion = menu()

        match opcion:
            case "1":
                handle_agregar_producto()
            case "2":
                handle_buscar_producto()
            case "3":
                handle_actualizar_precio()
            case "4":
                handle_eliminar_producto()
            case "5":
                handle_valor_total()
            case "6":
                handle_mostrar_inventario()
            case "7":
                print("\n👋 Saliendo del programa. ¡Hasta luego!")
                print("------------------------------------------------------")
                break
            case _:
                print("\n❗ Opción inválida. Intente nuevamente.")
                print("------------------------------------------------------")

    except Exception as e:
        print(f"\n⚠️ Error: {e}.")
        print("------------------------------------------------------")
