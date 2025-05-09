def validar_nombre(mensaje):
    """
    Solicita al usuario un nombre válido.

    Requisitos:
    - No debe estar vacío.
    - No debe ser numérico.

    Parámetros:
        mensaje (str): Texto que se muestra como instrucción.

    Retorna:
        str: Nombre validado.
    """
    while True:
        nombre = input(mensaje).strip()
        if not nombre or nombre.isnumeric():
            print("❌ Nombre inválido. Ingrese un nombre válido.")
        else:
            return nombre


def validar_precio(mensaje):
    """
    Solicita al usuario un precio numérico válido.

    Requisitos:
    - Debe ser un número flotante.
    - Debe ser mayor que cero.

    Parámetros:
        mensaje (str): Texto que se muestra como instrucción.

    Retorna:
        float: Precio validado.
    """
    while True:
        try:
            precio = float(input(mensaje))
            if precio <= 0:
                print("❌ El precio debe ser mayor que cero.")
            else:
                return precio
        except ValueError:
            print("❌ Entrada no válida. Ingrese un número válido para el precio.")


def validar_cantidad(mensaje):
    """
    Solicita al usuario una cantidad entera válida.

    Requisitos:
    - Debe ser un número entero.
    - Debe ser mayor que cero.

    Parámetros:
        mensaje (str): Texto que se muestra como instrucción.

    Retorna:
        int: Cantidad validada.
    """
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor que cero.")
            else:
                return cantidad
        except ValueError:
            print("❌ Entrada no válida. Ingrese un número entero válido.")
