from producto import registrar_varios_productos
from compra import calcular_total_compra, aplicar_descuento, generar_recibo, nueva_compra
from Informacion import mostrar_informacion, buscar_producto_por_nombre, eliminar_producto

def menu():
    lista_productos = []
    
    while True:
        print("\n=== TIENDA ESCOLAR ===")
        print("1. Registrar productos")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Calcular total de compra")
        print("5. Eliminar un producto")
        print("6. Iniciar nueva compra")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            nuevos = registrar_varios_productos()
            lista_productos.extend(nuevos)
        elif opcion == "2":
            mostrar_informacion(lista_productos)
        elif opcion == "3":
            buscar_producto_por_nombre(lista_productos)
        elif opcion == "4":
            if not lista_productos:
                print("\nNo hay productos en la lista para calcular.")
            else:
                total = calcular_total_compra(lista_productos)
                print(f"\nTotal acumulado de la compra: ${total:,.2f}")
                
                porcentaje = 0.0
                total_final = total
                desc = input("¿Deseas aplicar descuento? (s/n): ").strip().lower()
                if desc == "s":
                    try:
                        porcentaje = float(input("Porcentaje de descuento: "))
                        total_final = aplicar_descuento(total, porcentaje)
                        print(f"Total final con descuento: ${total_final:,.2f}")
                    except ValueError:
                        print("Porcentaje no válido.")
                
                imprimir = input("¿Deseas generar el ticket de compra? (s/n): ").strip().lower()
                if imprimir == "s":
                    generar_recibo(lista_productos, total, total_final, porcentaje)
        elif opcion == "5":
            eliminar_producto(lista_productos)
        elif opcion == "6":
            nueva_compra(lista_productos)
            
        elif opcion == "7":
            print("¡Gracias por usar el sistema!")
            break
            
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
