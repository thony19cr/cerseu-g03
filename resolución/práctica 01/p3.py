nombre = input("Ingrese Nombre: ")
apellidos = input("Ingrese Apellidos: ")
edad = int(input("Ingrese edad: "))
dni = input("Ingrese DNI: ")

diccionario = {
  "Nombre": nombre,
  "Apellidos": apellidos,
  "Edad": edad,
  "DNI": dni
}
print(diccionario)

profesion = input("Ingrese Profesion: ")
diccionario['Profesion'] = profesion
print(diccionario)

del diccionario['DNI']
print("Se elimino DNI")
print(diccionario)