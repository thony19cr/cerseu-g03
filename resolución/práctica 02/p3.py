"""
3. Escribir un programa para gestionar los errores en Python

Reglas:
    - El programa deberá tener una función para ingresar dos datos los
    cuáles serán ingresado por consola.
    - Deberá tener una función en el caso haya una división entre cero y
    mencionar el error.
    - Deberá tener una función la cuál evaluará la suma de datos
    incorrectos.
    - Todas las funciones creadas tendrás la facultad de volver a pedir el
    número hasta que se ingrese correctamente.
"""


def cargarDatos():
    a = int(input("Ingrese su primer dato: "))
    b = int(input("Ingrese su primer dato: "))
    return [a, b]


def verificarDivisionCero():

    while True:
        try:
            datos = cargarDatos()
            resultado = datos[0]/datos[1]
            return resultado

        except ZeroDivisionError:
            print("No es posible realizar esta división!!")


def verificarSuma():
    while True:
        try:
            datos = cargarDatos()
            suma = datos[0] + datos[1]
            return suma
            break
        except (ValueError, TypeError):
            print("No es posible realizar la suma con ese tipo de dato ingresado!!")


print("La división es: {}".format(verificarDivisionCero()))
print("La suma es: {}".format(verificarSuma()))
