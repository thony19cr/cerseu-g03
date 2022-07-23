
"""Estructura de datos"""

"""Listas: Agregando un ítem al final de nuestra lista"""

lista = []
lista2 = []
"""Usando iteración con for"""

for item in range(5):
    lista.append(item*2)

print("El valor de mi lista es: {}".format(lista))



"""Podemos usar el for empezando con otro número y poniendo un límite"""
for item in range(6, 11):
    lista2.append(item)

print("El valor de mi lista2 es: {}".format(lista2))
