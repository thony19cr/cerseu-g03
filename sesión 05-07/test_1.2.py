
"""Bucle While"""

"""
Reglas: 

- Ingresar número enteros por teclado hasta que el usuario ingrese 1 
- Realizar la sumatoria de todos los número ingresados

"""

numero = int(input("Ingrese un número: "))

total = 0
while numero != 1:
   total = total + numero
   print("Mi suma hasta el momento es: {}".format(total))
   numero = int(input("Ingrese un número: "))

print("La sumatorio de todos tus números ingresado es: {}".format(total))
