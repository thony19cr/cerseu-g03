
"""Decoradores en Python"""
"""Creación de una función decoradora"""


def funcionA(funcionB):

    def funcionC(*args, **kwargs):
        print("Antes de ejecutar la función que para por parámetro")
        resultado = funcionB(*args, **kwargs)
        print(resultado)
        print("Después de ejecutar la función decorada")

    return funcionC


@funcionA
def suma(a, b, c, d):
    total = a + b + c + d
    return total


suma(30, 40, 100, 200)


# print(suma(30, 40, 100, 200))
