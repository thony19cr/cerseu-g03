
"""Uso del flujo condicional if"""

edad = int(input("Hola, por favor ingrese su edad"))
var1 = edad
var2 = 100.50
var3 = 30

if type(var1) == type(var3):
    print("El dato es tipo entero!!!")
    resultado = var1 + 10
    print("La edad del usuario dentro de 10 años será: {}".format(resultado))
else:
    print("El dato ingresado por el usuario no es entero")
