
"""Uso del for"""

ingenierias = ["software", "sistemas", "industrial", "electrónica", "química"]
i = 0


print("El tamaño de nuestroa lista es: {}".format(len(ingenierias)))

for ingenieria in ingenierias:

    print("Ingeniería {}".format(ingenieria))
    i = i + 1
    print("Esta es la vuelta número: {}".format(i))

print("Llegó al final de nuestro for")
