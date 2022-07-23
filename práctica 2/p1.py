"""1. Escriba un programa donde tendrá los siguientes requisitos:
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla)"""

"""Pregunta 01"""

"""
1. Escriba un programa donde tendrá los siguientes requisitos:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla)

"""


class Persona:

    def __init__(self, nombre, edad, nacionalidad="Peruana"):
            self.nombre = nombre
            self.edad = edad
            self.nacionalidad = nacionalidad

    def cumpleaños(self):
        try:
            self.edad += 1
        except TypeError:
            print("Ingresar tipo de dato correcto")

    def imprimir_edad(self):
        return self.edad


# Instanciar
persona = Persona("Carlos", 28)

persona.cumpleaños()
persona.cumpleaños()

print("Edad: {}".format(persona.imprimir_edad()))