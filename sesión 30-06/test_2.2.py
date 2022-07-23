
"""Ejercicios de Listas"""

"""Crear una lista con 10 valores aleatorios"""
"""Ordenar una lista de menor a myor"""

import random

miLista = []

for indice in range(1, 11):
    miLista.append(random.randint(10, 100))

print("Mi lista actual es: {}".format(miLista))

"""Ordanando nuestra lista"""
miLista.sort()

print("Mi lista ordenada es: {}".format(miLista))

for numero in miLista:
    print(numero)


