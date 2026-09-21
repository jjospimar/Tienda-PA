def mostrar_informacion(productos):
  if not productos:
      print("No hay productos registrados \n")
      return

      print(" Productos registrados ")
  for i, producto in enumerate(productos, start=1):
      print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")
      print(f"Total de productos: {len(productos)} \n")

def buscar_producto_por_nombre(productos):
  nombre_buscado = input("Escribe el nombre del producto que quieres buscar: ")
  for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"Encontrado: {producto['nombre']} - ${producto['precio']:.2f}\n")
            return
  print(f"No se encontró ningún producto con el nombre '{nombre_buscado}'.\n")

def eliminar_producto(productos):
  if not productos:
    print("No hay productos registrados para eliminar\n")
    return
    nombre_buscado=input("Escribe el nombre del producto a eliminar: ")
    for i, producto in enumerate(productos):
      if producto["nombre"].lower()==nombre_buscado.lower():
        eliminado = productos.pop(i)
        print("Producto '{eliminado['nombre']}' eliminado")
        return
    print("No se encontró el producto")
