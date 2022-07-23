
"""Estructura de datos"""
"""Diccionario"""
"""Eliminando un key de un diccionario"""

diccionario = {"nombre": "Python", "tipo": "Backend"}

print("Mi diccionario contiene: {}".format(diccionario))

del diccionario["tipo"]

print("Mi diccionario actualizado es: {}".format(diccionario))

del diccionario["nombre"]

print("Mi diccionario actualizado por segunda es: {}".format(diccionario))
