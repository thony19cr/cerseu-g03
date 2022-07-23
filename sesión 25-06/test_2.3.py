
"""Introducción a los diccionarios"""

"""Declarando nuestro primer diccionario"""

diccionario = {"nombre": "Carlos", "apellido": "Fernandez", "edad": 29}

print("El contenido de mi varaible diccionario es: {}".format(diccionario))

print("Bienvenido {} {} usted tiene {} años".format(diccionario['nombre'], diccionario['apellido'], diccionario["edad"]))


diccionario2 = {"nombre": "Andrea", "apellido": "Rosales", "cursos": ["Python", "Django", "UX"]}

print("Los cursos a lo que estás matriculados son: {}".format(diccionario2["cursos"]))

print("1er Curso: {}".format(diccionario2["cursos"][0]))
print("2do Curso: {}".format(diccionario2["cursos"][1]))
print("3er Curso: {}".format(diccionario2["cursos"][2]))


"""Adicional para introducción a Estructuras de control"""
i = 0
for key in diccionario2:
    if key == "cursos":
        for val in diccionario2[key]:
            print(diccionario2[key][i])
            i = i + 1  #Aumenta en 1 el valor de i