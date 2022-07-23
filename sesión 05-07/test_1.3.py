
"""Bucle While"""

"""
- Leer por teclado enteros positivos hasta que el usuario ingrese -1
- Imprimir la suma de todos los dígitos que lo componen

"""

numero = int(input("Ingrese un número positivo: "))
suma = 0

while numero != 0:
    digito = numero % 10
    suma = suma + digito
    print("digito {}".format(digito))
    print("suma {}".format(suma))
    numero = numero//10

    print("numero {}".format(numero))


print("La suma de los dígitos es: {}".format(suma))


