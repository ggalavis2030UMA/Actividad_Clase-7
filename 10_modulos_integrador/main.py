"""EJERCICIO 10 — Módulos e integración

Organiza la aplicación en tres módulos de esta carpeta:
- datos.py: contiene PRODUCTOS (ya entregado).
- operaciones.py: implementa generar_reporte siguiendo su enunciado.
- main.py: importa los datos y la función, y muestra los resultados con print.
No copies los datos ni la función dentro de este archivo.
No importes archivos de otros ejercicios.

Con PRODUCTOS, el reporte esperado es:
{"disponibles": ["cafe", "torta", "pan"],
 "valor_total": 180,
 "hay_agotados": True,
 "categorias": {"bebida", "postre", "comida"},
 "precios_con_recargo": [("cafe", 11.0), ("torta", 27.5), ("pan", 5.5)]}
El orden de los elementos del set puede cambiar.

Con [] se espera:
{"disponibles": [], "valor_total": 0, "hay_agotados": False,
 "categorias": set(), "precios_con_recargo": []}

Ejecuta desde la raíz: python 10_modulos_integrador/main.py
Añade otro ejemplo con print y su resultado esperado en un comentario.
Haz un commit: "Resuelve ejercicio 10".
"""

# Importamos la data desde datos.py
from datos import PRODUCTOS
# Importamos nuestra función desde operaciones.py
from operaciones import generar_reporte

# Descomentamos las líneas originales solicitadas
print(generar_reporte(PRODUCTOS))
print(generar_reporte([]))

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
productos_extra = [
    {"nombre": "agua", "precio": 2, "stock": 10, "categoria": "bebida"},
    {"nombre": "galleta", "precio": 3, "stock": 0, "categoria": "postre"}
]
print(generar_reporte(productos_extra))
# Resultado esperado: 
# {'disponibles': ['agua'], 'valor_total': 20, 'hay_agotados': True, 'categorias': {'bebida', 'postre'}, 'precios_con_recargo': [('agua', 2.2)]}