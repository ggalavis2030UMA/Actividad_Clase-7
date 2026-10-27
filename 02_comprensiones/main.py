"""EJERCICIO 02 — Preparar un catálogo

ENUNCIADO
Cada producto tiene nombre, precio y categoria. Los nombres son únicos.
Devuelve un diccionario con:
- disponibles: lista de nombres con precio <= 20, en el orden original.
- precios: diccionario nombre -> precio de todos los productos.
- categorias: set de todas las categorías.
Usa una comprensión para cada estructura. No uses ciclos explícitos.
No modifiques la entrada. Para [] devuelve las tres estructuras vacías.

Con los datos entregados se espera:
{"disponibles": ["cafe", "te"],
 "precios": {"cafe": 10, "torta": 25, "te": 8},
 "categorias": {"bebida", "postre"}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 02".
"""

def preparar_catalogo(productos):
    return {
        "disponibles": [p["nombre"] for p in productos if p["precio"] <= 20],
        "precios": {p["nombre"]: p["precio"] for p in productos},
        "categorias": {p["categoria"] for p in productos}
    }


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
productos = [
    {"nombre": "cafe", "precio": 10, "categoria": "bebida"},
    {"nombre": "torta", "precio": 25, "categoria": "postre"},
    {"nombre": "te", "precio": 8, "categoria": "bebida"},
]
print(preparar_catalogo(productos))
# Resultado esperado:
# {'disponibles': ['cafe', 'te'], 'precios': {'cafe': 10, 'torta': 25, 'te': 8}, 'categorias': {'bebida', 'postre'}}

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
productos_2 = [
    {"nombre": "libro", "precio": 15, "categoria": "papeleria"},
    {"nombre": "laptop", "precio": 1200, "categoria": "tecnologia"},
    {"nombre": "lapiz", "precio": 2, "categoria": "papeleria"},
    {"nombre": "mouse", "precio": 18, "categoria": "tecnologia"}
]
print(preparar_catalogo(productos_2))
# Resultado esperado:
# {'disponibles': ['libro', 'lapiz', 'mouse'], 'precios': {'libro': 15, 'laptop': 1200, 'lapiz': 2, 'mouse': 18}, 'categorias': {'papeleria', 'tecnologia'}}

# Ejemplo 3 (lista vacía)
productos_vacios = []
print(preparar_catalogo(productos_vacios))
# Resultado esperado:
# {'disponibles': [], 'precios': {}, 'categorias': set()}
