# ------------------ Sistema de Gestión de Inventario ------------------

def solicitar_nombre(mensaje):
    """Solicita y valida un nombre de producto no vacío ni numérico."""
    while True:
        nombre = input(mensaje).strip()
        if not nombre or nombre.isnumeric():
            print("Nombre inválido. Ingrese un nombre válido.")
        else:
            return nombre


def solicitar_precio(mensaje):
    """Solicita un precio numérico mayor que cero."""
    while True:
        try:
            precio = float(input(mensaje))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                return precio
        except ValueError:
            print("Entrada no válida. Ingrese un número válido para el precio.")


def solicitar_cantidad(mensaje):
    """Solicita una cantidad entera mayor que cero."""
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
            else:
                return cantidad
        except ValueError:
            print("Entrada no válida. Ingrese un número entero válido para la cantidad.")


def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario."""
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"✅ Producto '{nombre}' agregado con éxito.")
    return inventario


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre y lo retorna si existe."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    print(f"❌ Producto '{nombre}' no encontrado.")
    return None


def actualizar_precio(inventario, nombre, nuevo_precio):
    """Actualiza el precio de un producto si existe en el inventario."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        producto["precio"] = nuevo_precio
        print(f"🛠 Precio de '{nombre}' actualizado a ${nuevo_precio:.2f}.")


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario si existe."""
    for i, producto in enumerate(inventario):
        if producto["nombre"].lower() == nombre.lower():
            del inventario[i]
            print(f"🗑 Producto '{nombre}' eliminado.")
            return
    print(f"❌ Producto '{nombre}' no encontrado.")


def calcular_valor_total(inventario):
    """Calcula el valor total del inventario (precio x cantidad)."""
    total = sum(prod["precio"] * prod["cantidad"] for prod in inventario)
    return total


def mostrar_inventario(inventario):
    """Muestra el listado actual de productos en el inventario."""
    if not inventario:
        print("📦 El inventario está vacío.")
    else:
        print("\n📋 Inventario actual:")
        for producto in inventario:
            print(f"- {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
        print("----------------------------------------------------")


def menu():
    """Muestra el menú principal y retorna la opción del usuario."""
    print("\n📌 Menú de opciones:")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar inventario")
    print("7. Salir")
    return input("Seleccione una opción: ").strip()


# ------------------ Sistema de Gestión de Inventario ------------------

# ... [todas las funciones anteriores sin cambios, ya optimizadas] ...

# --------------------- PROGRAMA PRINCIPAL ---------------------

print("🔧 Bienvenido al sistema de gestión de inventario 🔧")
inventario = []

while True:
    try:
        opcion = menu()

        match opcion:
            case "1":
                print("\n------------------ Agregar Producto ------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto: ")
                precio = solicitar_precio("Ingrese el precio del producto: ")
                cantidad = solicitar_cantidad("Ingrese la cantidad: ")
                agregar_producto(inventario, nombre, precio, cantidad)
                print("------------------------------------------------------")

            case "2":
                print("\n------------------ Buscar Producto -------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto a buscar: ")
                producto = buscar_producto(inventario, nombre)
                if producto:
                    print(f"🔎 Encontrado: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
                print("------------------------------------------------------")

            case "3":
                print("\n---------------- Actualizar Precio -------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto a actualizar: ")
                nuevo_precio = solicitar_precio("Ingrese el nuevo precio: ")
                actualizar_precio(inventario, nombre, nuevo_precio)
                print("------------------------------------------------------")

            case "4":
                print("\n---------------- Eliminar Producto -------------------")
                nombre = solicitar_nombre("Ingrese el nombre del producto a eliminar: ")
                eliminar_producto(inventario, nombre)
                print("------------------------------------------------------")

            case "5":
                print("\n------------ Valor Total del Inventario -------------")
                total = calcular_valor_total(inventario)
                print(f"💰 Valor total del inventario: ${total:,.2f}")
                print("------------------------------------------------------")

            case "6":
                print("\n------------------ Mostrar Inventario ----------------")
                mostrar_inventario(inventario)
                print("------------------------------------------------------")

            case "7":
                print("\n------------------- Salida del Programa -------------------")
                print("👋 Saliendo del programa. ¡Hasta luego!")
                print("-----------------------------------------------------------")
                break

            case _:
                print("\n❗ Opción inválida. Intente nuevamente.")
                print("------------------------------------------------------")
    except Exception as e:
        print(f"\n⚠️ Error: {e}.")
        print("------------------------------------------------------")
