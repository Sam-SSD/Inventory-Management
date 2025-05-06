def solicitar_nombre(mensaje):
    """
    Solicita al usuario un nombre de producto y valida que:
    - No esté vacío
    - No sea completamente numérico
    """
    while True:
        nombre = input(mensaje).strip()
        if not nombre or nombre.isnumeric():
            print("Nombre inválido. Ingrese un nombre válido.")
        else:
            return nombre


def solicitar_precio(mensaje):
    """
    Solicita al usuario un precio flotante y valida que:
    - Sea un número
    - Sea mayor que cero
    """
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
    """
    Solicita al usuario una cantidad entera y valida que:
    - Sea un entero
    - Sea mayor que cero
    """
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
            else:
                return cantidad
        except ValueError:
            print("Entrada no válida. Ingrese un número entero válido.")
