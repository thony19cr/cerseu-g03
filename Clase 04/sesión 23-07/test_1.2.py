
"""Decoradores en Python"""

"""Creación de una función decoradora"""


def funcionA(funcionB):

    def funcionC(*args, **kwargs):
        print("Antes de ejecutar la función a decorar")
        resultado = funcionB(*args, **kwargs)
        print("Después de ejecutar la función a decorar")
        return resultado
    return funcionC


@funcionA
def saludar(name, lastname, age):
    print("Hola {} {}, usted tiene {} años".format(name, lastname, age))


nombre = input("Ingrese nu nombre por favor: ")
apellido = input("Ingrese su apellido ahora: ")
edad = input("Ingrese su edad finalmente: ")
saludar(nombre, apellido, edad)
