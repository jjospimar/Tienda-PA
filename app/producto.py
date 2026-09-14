def registrar_producto():
    """Pide al usuario el nombre y precio de un producto y lo devuelve."""
    nombre = input("Nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Precio del producto: "))
            break
        except ValueError:
            print("Por favor ingresa un número válido para el precio.")
    
    return {"nombre": nombre, "precio": precio}


def registrar_varios_productos():
    """Permite registrar varios productos hasta que el usuario decida parar."""
    productos = []
    
    while True:
        producto = registrar_producto()
        productos.append(producto)
        print(f"Producto '{producto['nombre']}' registrado con éxito.\n")
        
        continuar = input("¿Deseas registrar otro producto? (s/n): ").lower()
        if continuar != "s":
            break
    
    return productos
