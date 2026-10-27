"""EJERCICIO 05 — Subtotales de pedidos

ENUNCIADO
Cada pedido es una tupla (producto, precio_unitario, cantidad).
Usa map con lambda para calcular precio_unitario * cantidad de cada pedido.
Devuelve una lista en el orden original. Convierte el resultado de map con list.
No uses ciclos ni comprensiones. Los valores son enteros no negativos.
Para [] devuelve [].

Entrada: [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
Resultado esperado: [20, 24, 25]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 05".
"""

def calcular_subtotales(pedidos):
    # map aplica la lambda a cada tupla 'pedido' de la lista
    # lambda toma la tupla, multiplica su elemento en el índice 1 (precio) por el índice 2 (cantidad)
    # Finalmente, convertimos el objeto map devuelto en una lista con list()
    return list(map(lambda pedido: pedido[1] * pedido[2], pedidos))


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
pedidos = [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
print(calcular_subtotales(pedidos))
# Resultado esperado: [20, 24, 25]

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
pedidos_2 = [("jugo", 5, 4), ("sandwich", 12, 2), ("galleta", 3, 0)]
print(calcular_subtotales(pedidos_2))
# Resultado esperado: [20, 24, 0]

# Ejemplo 3 (lista vacía)
pedidos_vacios = []
print(calcular_subtotales(pedidos_vacios))
# Resultado esperado: []