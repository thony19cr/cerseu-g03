
"""Estructura de datos"""

"""Listas: Cantidad de veces que se repite un elemento en una lista"""

varLista = ["Python", "PHP", "Ruby"]

varLista.append("Python")
varLista.append("Python")
varLista.append("Ruby")

print("Mi nueva lista es: {}".format(varLista))
print("La cantidad de veces que se repite 'Python' es: {}".format(varLista.count("Python")))
print("La cantidad de veces que se repite 'Ruby' es: {}".format(varLista.count("Ruby")))
print("La cantidad de veces que se repite '1000' es: {}".format(varLista.count(1000)))
