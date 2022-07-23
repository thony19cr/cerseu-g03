
"""Manejo de cadenas"""

cadena = "Conexión a base de datos con Python"

cadena2 = cadena.replace(cadena[0:6], "cccc")

print("Cadena con reemplazos tiene el siguiente valor: {}".format(cadena2))

"""Elminando espacion en blanco antes de mi cadena"""

cadena3 = "               Conexión a base de datos con Python"
print("Mi valor original de mi variable cadena3 es: {}".format(cadena3))

cadena4 = cadena3.lstrip()
print("Mi cadena con espacios en blanco eliminado es: {}".format(cadena4))

cadena5 = "Conexión a base de datos                "

cadena6 = cadena5.rstrip()
print("Mi cadena con espacios en blanco eliminado es: {}".format(cadena6))
