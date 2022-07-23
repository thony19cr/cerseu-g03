"""
1. Escriba un programa donde tendrá los siguientes requisitos:

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
    registrado esta persona (Mostrar por pantalla)
"""

from datetime import date


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = 'Peruana'
        self.hRegistro = ""

    def cumpleanios(self):
        self.edad += 1

    def fechaRegistro(self):
        today = date.today()
        day = today.day
        month = today.month
        year = today.year
        self.hRegistro = "{} / {} / {}".format(day, month, year)
        return self.hRegistro


persona_random = Persona('Jacinto', 20)
persona_random.cumpleanios()
persona_random.cumpleanios()
persona_random.cumpleanios()
print("La edad actualizada de la persona es:", persona_random.edad)

print("La fecha de su registro fue en: ", persona_random.fechaRegistro())