def mostrar_informacion(productos):
  if not productos:
    print("No hay productos registrados \n")
    return

print(" Productos registrados ")
for i, producto in enumerate(productos, start=1):
  print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")
