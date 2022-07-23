
"""Uso del flujo condicional if"""

edad = int(input("¿Cuál es su edad?: "))

if 0 < edad < 18:
    print("Es usted menor de edad")
elif 18 <= edad <= 64:
    print("Es usted mayor de edad")
elif 120 > edad > 65:
    print("Es usted una persona de la tercera edad")
else:
    print("La edad que ingresaste es incorrecta!!")
