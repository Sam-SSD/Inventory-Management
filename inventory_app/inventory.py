class Inventario:
    def __init__(self):
        # Inicializa la lista de productos vacía
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        """
        Agrega un nuevo producto al inventario si el nombre no está duplicado.
        La comparación no distingue mayúsculas/minúsculas.
        Cada producto se representa como un diccionario con nombre, precio y cantidad.
        """
        for p in self.productos:
            if p["nombre"].lower() == nombre.lower():
                print(f"⚠️ Ya existe un producto con el nombre '{nombre}'. No se agregó.")
                return
        self.productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"✅ Producto '{nombre}' agregado con éxito.")

    def buscar_producto(self, nombre):
        """
        Busca un producto en el inventario por su nombre (no sensible a mayúsculas).
        Retorna el producto completo si lo encuentra, o None si no existe.
        """
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                return producto
        print(f"❌ Producto '{nombre}' no encontrado.")
        return None

    def actualizar_precio(self, nombre, nuevo_precio):
        """
        Actualiza el precio de un producto ya existente.
        Usa la función de búsqueda para validar su existencia.
        """
        producto = self.buscar_producto(nombre)
        if producto:
            producto["precio"] = nuevo_precio
            print(f"🛠 Precio de '{nombre}' actualizado a ${nuevo_precio:,.2f}.")

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario si se encuentra.
        Usa enumeración para poder eliminar por índice en caso de coincidencia.
        """
        for i, producto in enumerate(self.productos):
            if producto["nombre"].lower() == nombre.lower():
                del self.productos[i]
                print(f"🗑 Producto '{nombre}' eliminado.")
                return
        print(f"❌ Producto '{nombre}' no encontrado.")

    def calcular_valor_total(self):
        """
        Calcula el valor total del inventario sumando el producto de precio x cantidad por artículo.
        Retorna el total como número flotante.
        """
        return sum(p["precio"] * p["cantidad"] for p in self.productos)

    def mostrar_inventario(self):
        """
        Muestra el contenido actual del inventario en formato legible.
        Si está vacío, avisa al usuario.
        """
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for p in self.productos:
                print(f"- {p['nombre']} | Precio: ${p['precio']:,.2f} | Cantidad: {p['cantidad']}")
