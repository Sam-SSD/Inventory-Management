class Inventario:
    def __init__(self):
        # Lista principal que almacena los productos como diccionarios
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        """
        Agrega un nuevo producto al inventario si no existe un nombre duplicado (no sensible a mayúsculas).

        Parámetros:
            nombre (str): Nombre del producto.
            precio (float): Precio unitario.
            cantidad (int): Cantidad disponible.
        """
        for p in self.productos:
            if p["nombre"].lower() == nombre.lower():
                print(f"⚠️ Ya existe un producto con el nombre '{nombre}'. No se agregó.")
                return

        self.productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        print(f"✅ Producto '{nombre}' agregado con éxito.")

    def buscar_producto(self, nombre):
        """
        Busca un producto en el inventario por nombre (no sensible a mayúsculas).

        Parámetros:
            nombre (str): Nombre del producto a buscar.

        Retorna:
            dict: El producto si se encuentra, o None si no existe.
        """
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                return producto
        print(f"❌ Producto '{nombre}' no encontrado.")
        return None

    def actualizar_precio(self, nombre, nuevo_precio):
        """
        Actualiza el precio de un producto si existe.

        Parámetros:
            nombre (str): Nombre del producto.
            nuevo_precio (float): Nuevo precio a asignar.
        """
        producto = self.buscar_producto(nombre)
        if producto:
            producto["precio"] = nuevo_precio
            print(f"🛠 Precio de '{nombre}' actualizado a ${nuevo_precio:,.2f}.")

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario si existe.

        Parámetros:
            nombre (str): Nombre del producto a eliminar.
        """
        for i, producto in enumerate(self.productos):
            if producto["nombre"].lower() == nombre.lower():
                del self.productos[i]
                print(f"🗑 Producto '{nombre}' eliminado.")
                return
        print(f"❌ Producto '{nombre}' no encontrado.")

    def calcular_valor_total(self):
        """
        Calcula el valor total del inventario como la suma de (precio * cantidad) por producto.

        Retorna:
            float: Valor total del inventario.
        """
        return sum(p["precio"] * p["cantidad"] for p in self.productos)

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario con su precio y cantidad disponibles.
        """
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for p in self.productos:
                print(f"- {p['nombre']} | Precio: ${p['precio']:,.2f} | Cantidad: {p['cantidad']}")
