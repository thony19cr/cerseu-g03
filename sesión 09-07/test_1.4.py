"""Programación Orientada a Objetos"""
"""Herencia múltiple entre clases"""

class Carro(object):
    """Atributos"""
    ruedas = 4

    """Contructor: Valores que va a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        print("Ingresó al padre Carro!!")
        super(Carro, self).__init__()
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad


class CarroSedan(object):

    def __init__(self):
        print("Ingresó al padre Carro Sedan!!")
        super(CarroSedan, self).__init__()
        self.altura = 1.70


class CarroVolador(Carro, CarroSedan):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carVolador = CarroVolador("Negro", 50)
carVolador2 = CarroVolador("Azul", 25)
"""Herencia del primer padre"""
print("La velocidad inicial de mi carro volador es: {}".format(carVolador.color))

"""Herencia de la segunda clase padre"""
print("La altura de mi carro volador es: {}".format(carVolador.altura))
