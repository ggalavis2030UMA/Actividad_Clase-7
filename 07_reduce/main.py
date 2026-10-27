"""EJERCICIO 07 — Total de ventas

ENUNCIADO
Cada pedido es una tupla (producto, precio_unitario, cantidad).
Usa map con lambda para obtener los subtotales y reduce con lambda para sumarlos.
Importa reduce del módulo functools. Usa 0 como valor inicial de reduce.
No uses sum, ciclos ni comprensiones. Los valores son enteros no negativos.
Para [] devuelve 0.

Entrada: [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
Resultado esperado: 69

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 07".
"""

# Importamos reduce desde la librería functools de Python
from functools import reduce

def total_ventas(pedidos):
    # map: calcula el subtotal (precio * cantidad) de cada tupla
    # reduce: va sumando cada subtotal calculado, empezando desde 0
    return reduce(
        lambda acumulador, subtotal: acumulador + subtotal, 
        map(lambda pedido: pedido[1] * pedido[2], pedidos), 
        0
    )


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
pedidos = [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
print("Total ejemplo 1:", total_ventas(pedidos))
# Resultado esperado: 69 (20 + 24 + 25)

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
pedidos_2 = [("empanada", 2, 5), ("agua", 1, 3)]
print("Total ejemplo 2:", total_ventas(pedidos_2))
# Resultado esperado: 13 (10 + 3)

# Ejemplo 3 (lista vacía)
pedidos_vacios = []
print("Total vacío:", total_ventas(pedidos_vacios))
# Resultado esperado: 0
