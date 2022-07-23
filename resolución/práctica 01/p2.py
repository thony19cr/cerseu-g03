import random
listaRandom = []

for indice in range(1, 11):
    listaRandom.append(random.randint(1, 10))

print(listaRandom)
print("El valor cuadrado es: {} y el valor cubo es: {}".format(listaRandom**2, listaRandom**3))
