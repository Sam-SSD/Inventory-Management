from inventory import Inventario
from utils import solicitar_nombre, solicitar_precio, solicitar_cantidad


def menu():
    """
    Imprime las opciones disponibles para el usuario y solicita la opción elegida.
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
inventario = Inventario()  # Se crea una instancia del inventario

while True:
    try:
        opcion = menu()

        match opcion:
            case "1":
                print("\n------------------ Agregar Producto ------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto: ")
                precio = solicitar_precio("Ingrese el precio del producto: ")
                cantidad = solicitar_cantidad("Ingrese la cantidad: ")
                inventario.agregar_producto(nombre, precio, cantidad)
                print("------------------------------------------------------")

            case "2":
                print("\n------------------ Buscar Producto -------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(
                        f"🔎 Encontrado: {producto['nombre']} | Precio: ${producto['precio']:,.2f} | Cantidad: {producto['cantidad']}")
                print("------------------------------------------------------")

            case "3":
                print("\n---------------- Actualizar Precio -------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto a actualizar: ")
                nuevo_precio = solicitar_precio("Ingrese el nuevo precio: ")
                inventario.actualizar_precio(nombre, nuevo_precio)
                print("------------------------------------------------------")

            case "4":
                print("\n---------------- Eliminar Producto -------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)
                print("------------------------------------------------------")

            case "5":
                print("\n------------ Valor Total del Inventario -------------")
                total = inventario.calcular_valor_total()
                print(f"💰 Valor total del inventario: ${total:,.2f}")
                print("------------------------------------------------------")

            case "6":
                print("\n------------------ Mostrar Inventario ----------------")
                inventario.mostrar_inventario()
                print("------------------------------------------------------")

            case "7":
                print("\n👋 Saliendo del programa. ¡Hasta luego!")
                print("------------------------------------------------------")
                break

            case _:
                print("\n❗ Opción inválida. Intente nuevamente.")
                print("------------------------------------------------------")

    except Exception as e:
        # Captura cualquier error no controlado y evita que el programa se caiga
        print(f"\n⚠️ Error: {e}.")
        print("------------------------------------------------------")
