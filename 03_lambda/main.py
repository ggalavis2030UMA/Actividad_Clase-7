"""EJERCICIO 03 — Precios con recargo

ENUNCIADO
Dentro de la función, define una lambda que reciba un precio y devuelva
ese precio con un recargo del 10 %, redondeado a dos decimales con round.
Aplica la lambda mediante un ciclo y devuelve una lista.
No uses map todavía. Los precios son no negativos. No modifiques la entrada.
Para [] devuelve [].

Entrada: [10, 20, 35]
Resultado esperado: [11.0, 22.0, 38.5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 03".
"""

def calcular_importes(precios):
    # Definimos la función lambda para sumar el 10% y redondear a 2 decimales
    recargo = lambda precio: round(precio * 1.10, 2)
    
    # Creamos una nueva lista para no modificar la original
    precios_actualizados = []
    
    # Usamos un ciclo for para aplicar la lambda a cada precio
    for p in precios:
        precios_actualizados.append(recargo(p))
        
    return precios_actualizados


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
precios = [10, 20, 35]
print(calcular_importes(precios))
# Resultado esperado: [11.0, 22.0, 38.5]

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
precios_2 = [15.50, 99.99, 0]
print(calcular_importes(precios_2))
# Resultado esperado: [17.05, 109.99, 0.0]

# Ejemplo 3 (lista vacía)
precios_vacios = []
print(calcular_importes(precios_vacios))
# Resultado esperado: []