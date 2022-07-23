
"""Decoradores en Python"""

"""Creación de una función decoradora"""


def funcionA(funcionB):
    """Función interna de la función decoradora"""

    def funcionC():
        print("1. Antes de ejecutar la función a decorar\n")
        funcionB()
        print("\n2. Después de ejecutar la función a decorar")

    return funcionC()


@funcionA
def saludar():
    print("Hola Pythonista!!")

# saludar()
