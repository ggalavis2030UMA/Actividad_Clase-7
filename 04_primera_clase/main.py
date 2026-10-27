"""EJERCICIO 04 — Funciones como valores y argumentos

ENUNCIADO
Completa aplicar_operacion: recibe una lista y una función; aplica esa
función a cada elemento usando un ciclo y devuelve una lista.
Completa transformar: crea un diccionario de funciones lambda con las claves
"doble", "cuadrado" y "negativo". Usa aplicar_operacion para obtener
un diccionario con esas mismas claves y las listas transformadas.
No uses map ni modifiques la lista original.
Con [] cada lista del resultado debe estar vacía.

Entrada de transformar: [1, 2, 3]
Resultado esperado:
{"doble": [2, 4, 6], "cuadrado": [1, 4, 9], "negativo": [-1, -2, -3]}

Entrada de aplicar_operacion: [2, 4] y una función que sume 1.
Resultado esperado: [3, 5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 04".
"""

def aplicar_operacion(valores, operacion):
    # Creamos una lista nueva para no modificar la original
    resultado = []
    # Recorremos cada valor, le aplicamos la función y lo guardamos
    for v in valores:
        resultado.append(operacion(v))
    return resultado


def transformar(valores):
    # Diccionario donde los VALORES son funciones lambda
    funciones = {
        "doble": lambda x: x * 2,
        "cuadrado": lambda x: x ** 2,
        "negativo": lambda x: -x
    }
    
    # Diccionario para guardar las listas resultantes
    resultado_final = {}
    
    # Recorremos el diccionario de funciones
    for clave, funcion in funciones.items():
        # Usamos nuestra función auxiliar pasando la lista y la lambda correspondiente
        resultado_final[clave] = aplicar_operacion(valores, funcion)
        
    return resultado_final


# Ejemplo de uso: 
valores = [1, 2, 3]
print("Transformar:", transformar(valores))
# Resultado esperado: {'doble': [2, 4, 6], 'cuadrado': [1, 4, 9], 'negativo': [-1, -2, -3]}

# Ejemplo específico pedido en el enunciado para aplicar_operacion
print("Aplicar suma:", aplicar_operacion([2, 4], lambda x: x + 1))
# Resultado esperado: [3, 5]

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
valores_2 = [5, 0, -2]
print("Transformar 2:", transformar(valores_2))
# Resultado esperado: 
# {'doble': [10, 0, -4], 'cuadrado': [25, 0, 4], 'negativo': [-5, 0, 2]}

# Ejemplo 3 (lista vacía)
valores_vacios = []
print("Transformar vacío:", transformar(valores_vacios))
# Resultado esperado: 
# {'doble': [], 'cuadrado': [], 'negativo': []}