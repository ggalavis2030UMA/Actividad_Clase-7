"""EJERCICIO 06 — Revisión del inventario

ENUNCIADO
Cada producto tiene nombre y stock (entero no negativo).
Devuelve un diccionario con:
- reponer: lista de nombres con stock < 5, en el orden original.
- hay_agotados: booleano que indica si algún stock es igual a 0.
Usa filter con lambda para seleccionar, map con lambda para obtener nombres,
y any sobre map con lambda para detectar agotados.
No uses ciclos ni comprensiones ni modifiques los datos.
Para [] devuelve {"reponer": [], "hay_agotados": False}.

Con los datos entregados se espera:
{"reponer": ["te", "torta"], "hay_agotados": True}
Un producto con stock igual a 5 no debe aparecer en reponer.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 06".
"""

def revisar_stock(productos):
    # filter + lambda: selecciona solo los diccionarios con stock < 5
    # map + lambda: extrae el "nombre" de esos diccionarios filtrados
    # list(): convierte el resultado final en una lista visible
    reponer = list(
        map(lambda p: p["nombre"], 
            filter(lambda p: p["stock"] < 5, productos)
        )
    )
    
    # map + lambda: convierte cada diccionario en True (si stock == 0) o False (si stock != 0)
    # any(): devuelve True si al menos hay un True en todo el resultado anterior
    hay_agotados = any(
        map(lambda p: p["stock"] == 0, productos)
    )
    
    return {
        "reponer": reponer,
        "hay_agotados": hay_agotados
    }


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
productos = [
    {"nombre": "cafe", "stock": 8},
    {"nombre": "te", "stock": 0},
    {"nombre": "torta", "stock": 3},
]
print(revisar_stock(productos))
# Resultado esperado: {'reponer': ['te', 'torta'], 'hay_agotados': True}

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
productos_2 = [
    {"nombre": "agua", "stock": 5},
    {"nombre": "jugo", "stock": 10},
    {"nombre": "refresco", "stock": 50}
]
print(revisar_stock(productos_2))
# Resultado esperado: {'reponer': [], 'hay_agotados': False}

# Ejemplo 3 (lista vacía)
productos_vacios = []
print(revisar_stock(productos_vacios))
# Resultado esperado: {'reponer': [], 'hay_agotados': False}