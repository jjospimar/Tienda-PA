
def calcular_total_compra(productos):
    if not productos:
        return 0.0

    total_acumulado = 0.0

    for producto in productos:
        precio_unitario = producto.get("precio", 0.0)
        cantidad_unidades = producto.get("cantidad", 1)
        total_acumulado += precio_unitario * cantidad_unidades

    return total_acumulado


def aplicar_descuento(total_acumulado, porcentaje_descuento):
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        return total_acumulado

    monto_descuento = total_acumulado * (porcentaje_descuento / 100.0)
    return total_acumulado - monto_descuento


if __name__ == "__main__":
    datos_prueba = [
        {"precio": 5000, "cantidad": 2},
        {"precio": 1200, "cantidad": 3}
    ]

    total_obtenido = calcular_total_compra(datos_prueba)
    print(f"Total calculado: ${total_obtenido:,.2f}")

    total_con_desc = aplicar_descuento(total_obtenido, 10)
    print(f"Total con 10% descuento: ${total_con_desc:,.2f}")

def generar_recibo(productos, total_acumulado, total_final, porcentaje_descuento=0):
    print("\n" + "="*35)
    print("        TIENDA ESCOLAR - RECIBO")
    print("="*35)
    for prod in productos:
        precio = prod.get("precio", 0.0)
        print(f"- {prod['nombre']:<18} ${precio:>7.2f}")
    print("-" * 35)
    print(f"Subtotal:           ${total_acumulado:>8.2f}")
    if porcentaje_descuento > 0:
        monto_desc = total_acumulado - total_final
        print(f"Descuento ({porcentaje_descuento}%):      -${monto_desc:>8.2f}")
    print(f"TOTAL A PAGAR:      ${total_final:>8.2f}")
    print("="*35)

def nueva_compra(productos):
    if not productos:
        print("No hay productos registrados")
        return

    confirmacion = input("Estás seguro de que deseas iniciar una nueva compra y vaciar la lista actual? (s/n): ").strip().lower()
    if confirmacion == "s":
        productos.clear()  
        print("Se ha reiniciado la compra. La lista de productos ahora está vacía.\n")
    else:
        print(" Se conservan los productos actuales.\n")
        
