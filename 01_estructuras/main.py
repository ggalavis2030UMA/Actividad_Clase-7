"""EJERCICIO 01 — Resumen de ventas

ENUNCIADO
Recibes una lista de tuplas (producto, cantidad). Devuelve un diccionario con:
- productos: set con los nombres vendidos.
- unidades: total de unidades vendidas.
- por_producto: diccionario con las cantidades acumuladas por producto.
Usa ciclos, un set y un diccionario. No modifiques la entrada.
Las cantidades son enteros positivos. Para [] devuelve estructuras vacías y total 0.

Ejemplo:
Entrada: [("cafe", 2), ("te", 1), ("cafe", 3)]
Resultado: {"productos": {"cafe", "te"}, "unidades": 6,
            "por_producto": {"cafe": 5, "te": 1}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 01".
"""

def resumir_ventas(ventas):
    productos_set = set()
    total_unidades = 0
    por_producto_dict = {}

    for producto, cantidad in ventas:
        productos_set.add(producto)
        total_unidades += cantidad
        
        if producto in por_producto_dict:
            por_producto_dict[producto] += cantidad
        else:
            por_producto_dict[producto] = cantidad

    return {
        "productos": productos_set,
        "unidades": total_unidades,
        "por_producto": por_producto_dict
    }


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
ventas = [("cafe", 2), ("te", 1), ("cafe", 3)]
print(resumir_ventas(ventas))

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
ventas_2 = [("manzana", 5), ("pera", 2), ("manzana", 3), ("uva", 1)]
print(resumir_ventas(ventas_2))
# Resultado esperado: 
# {'productos': {'pera', 'manzana', 'uva'}, 'unidades': 11, 'por_producto': {'manzana': 8, 'pera': 2, 'uva': 1}}

# Ejemplo 3 (lista vacía)
ventas_vacias = []
print(resumir_ventas(ventas_vacias))
# Resultado esperado:
# {'productos': set(), 'unidades': 0, 'por_producto': {}}