# inventory.py

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        self.productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"✅ Producto '{nombre}' agregado con éxito.")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                return producto
        print(f"❌ Producto '{nombre}' no encontrado.")
        return None

    def actualizar_precio(self, nombre, nuevo_precio):
        producto = self.buscar_producto(nombre)
        if producto:
            producto["precio"] = nuevo_precio
            print(f"🛠 Precio de '{nombre}' actualizado a ${nuevo_precio:,.2f}.")

    def eliminar_producto(self, nombre):
        for i, producto in enumerate(self.productos):
            if producto["nombre"].lower() == nombre.lower():
                del self.productos[i]
                print(f"🗑 Producto '{nombre}' eliminado.")
                return
        print(f"❌ Producto '{nombre}' no encontrado.")

    def calcular_valor_total(self):
        return sum(p["precio"] * p["cantidad"] for p in self.productos)

    def mostrar_inventario(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for p in self.productos:
                print(f"- {p['nombre']} | Precio: ${p['precio']:,.2f} | Cantidad: {p['cantidad']}")
