"""
MÓDULO: compra.py
RESPONSABLE: Santiago Mora (Cálculo del total de compra)

"""

def calcular_total_compra((parametro lista productos)):
    if not (parametro lista productos):
        return 0.0

    total_acumulado = 0.0

    for producto in (parametro lista productos):
        precio_unitario = producto.get("(clave precio)", 0.0)
        cantidad_unidades = producto.get("(clave cantidad)", 1)
        total_acumulado += precio_unitario * cantidad_unidades

    return total_acumulado


def aplicar_descuento(total_acumulado, (parametro porcentaje descuento)):
    if (parametro porcentaje descuento) < 0 or (parametro porcentaje descuento) > 100:
        return total_acumulado

    monto_descuento = total_acumulado * ((parametro porcentaje descuento) / 100.0)
    return total_acumulado - monto_descuento


if __name__ == "__main__":
    datos_prueba = [
        {"(clave precio)": 5000, "(clave cantidad)": 2},
        {"(clave precio)": 1200, "(clave cantidad)": 3}
    ]

    total_obtenido = calcular_total_compra(datos_prueba)
    print(f"Total calculado: ${total_obtenido:,.2f}")

    total_con_desc = aplicar_descuento(total_obtenido, 10)
    print(f"Total con 10% descuento: ${total_con_desc:,.2f}")
