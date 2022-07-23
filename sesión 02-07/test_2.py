
"""Conversión de datos"""

var1 = "2023"
var2 = type(int(var1))

var3 = "A20232022"
"""Esto no es posible porque el valor contiene una letra"""
var4 = type(int(var3))

print("El tipo de dato de mi var2 es: {}".format(var2))

"""Mostrará un error porque no lo puede convertir a entero"""
print("El tipo de dato de mi var2 es: {}".format(var4))
