"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear el
siguiente programa:

Reglas:
    - Agregar un atributo saldo a la clase persona.
    - Crear un método transferencia(self, persona2, monto)
    - El saldo deberá representar el dinero que tiene la otra persona
    - El método transferencia hace que la Persona que llame al método pueda
    transferir la cantidad monto al objeto Persona2
    - Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
    imprimir “Saldo insuficiente”
"""

class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo  #Encapsulamiento
        self.nacionalidad = 'Peruano'

    def cumpleanios(self):
        self.edad += 1


class Usuario(Persona):
    def transferencia(self, otra_persona, monto):
        if monto > self.__saldo:
            print('Saldo insuficiente!!!')
        else:
            self.__saldo -= monto
            otra_persona.__saldo += monto


primera_persona = Usuario('Cris', 20, 400)
segunda_persona = Usuario('Rick', 22, 600)