def registrar_producto():
    nombre = input("Nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Precio del producto: "))
            break
        except ValueError:
            print("Por favor ingresa un número válido para el precio.")
    
    return {"nombre": nombre, "precio": precio}

def registrar_varios_productos():
    productos = []
    
    registrando = True
    while registrando:
        producto = registrar_producto()
        productos.append(producto)
        print(f"Producto '{producto['nombre']}' registrado con éxito.\n")
        
        continuar = input("¿Deseas registrar otro producto? (s/n): ").strip().lower()
        if continuar != "s":
            registrando = False
    
    return productos
