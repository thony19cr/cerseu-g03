
"""E/S Python"""
"""Entradas en Python"""

usuario = input("Ingrese su nombre de usario: ")
nombre = input("¿Cuál es su nombre? ")

print("¡Bienvenido {}!".format(nombre))

telefono = input("Ingrese su número de celular: ")

print("{} tiene el siguiente número telefónico: {}".format(nombre, telefono))


edad = int(input("¿Cuál es su edad?: "))

print(type(edad))
print("Usted tiene {} años".format(edad))


"""Usando condicionales"""
if edad >= 18:
    print("Usted es mayor de edad")
elif edad < 18:
    print("Usted es menor de edad")

