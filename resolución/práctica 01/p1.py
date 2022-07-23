import random
ListaRandom = []
ListaRandomCuad = []
ListaRandomCubo = []

#LISTA RANDOM 10 VALORES
for indice in range (1,10):
    ListaRandom.append(random.randint(1,10))
    print(ListaRandom)

#lISTA RANDOM 10 VALORES CUADRADOR
for indice in range (1,10):
    ListaRandomCuad.append(random.randint(1,10))
for valor in ListaRandomCuad:
    print("el valor al cuadrado es: {}".format(valor**2))

#lISTA RANDOM 10 VALORES CUBOS
for indice in range (1,10):
    ListaRandomCubo.append(random.randint(1,10))
for valor in ListaRandomCubo:
    print("el valor al Cubo es: {}".format(valor**3))