
"""Bucle While"""

numero = int(input("Ingrese un número menor de 10: "))

while numero < 10:
    numero += 1  #Aumenta en uno el valor de la varaible "numero"
    print("El número es: {}".format(numero))
    if numero == 8:
        print("Número encotrado!!")
        break   #Break: Nos permite romper el bucle ants que llegué al tope de la condición.

print("Llegó al final del búcle while")