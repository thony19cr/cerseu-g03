
"""Uso de *args"""


def multiplica(*args):
    valor = 1
    for i in args:
        print(i)
        valor = valor * i
    return valor


num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
print("El resultado total es: {}".format(multiplica(num1, num2, 10, 2, 1000)))
print("Fin módulo I")
