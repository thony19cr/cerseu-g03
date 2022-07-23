"""3. Escribir un programa para gestionar los errores en Python
Reglas:
- El programa deberá tener una función para ingresar dos datos los
cuáles serán ingresado por consola.
- Deberá tener una función en el caso haya una división entre cero y
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos.
- Todas las funciones creadas tendrás la facultad de volver a pedir el
número hasta que se ingrese correctamente. """

"""Pregunta 03"""
"""solucion"""
value_1 = int(input("Ingrese un número: "))
value_2 = int(input("Ingrese otro número: "))

def dividir(number_1, number_2):
    try:
        division = number_1 / number_2
        return division
    except ZeroDivisionError:
        print("Error: No se pude dividir un numero entre cero")

print("División: {}".format(dividir(value_1, value_2)))