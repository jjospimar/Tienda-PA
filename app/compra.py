
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
