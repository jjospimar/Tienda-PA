from producto import registrar_varios_productos
from compra import calcular_total_compra, aplicar_descuento
from Informacion import mostrar_informacion, buscar_producto_por_nombre

def menu():
    lista_productos = []
    
    while True:
        print("\n=== TIENDA ESCOLAR ===")
        print("1. Registrar productos")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Calcular total de compra")
        print("5. Eliminar un producto")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            lista_productos.extend(registrar_varios_productos())
        elif opcion == "2":
            mostrar_informacion(lista_productos)
        elif opcion == "3":
            buscar_producto_por_nombre(lista_productos)
        elif opcion == "4":
            total = calcular_total_compra(lista_productos)
            print(f"\nTotal acumulado de la compra: ${total:,.2f}")
            
            desc = input("¿Deseas aplicar descuento? (s/n): ").lower()
            if desc == "s":
                porcentaje = float(input("Porcentaje de descuento: "))
                total_final = aplicar_descuento(total, porcentaje)
                print(f"Total final con descuento: ${total_final:,.2f}")
        elif opcion == "5":
            eliminar_producto(lista_productos)
        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
        break

if __name__ == "__main__":
    menu()
