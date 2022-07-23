"""2. Usando el concepto de herencia y encapsulación (para saldo) para crear el
siguiente programa:
Reglas:

- Agregar un atributo saldo a la clase persona.
- Crear un método transferencia(self, persona2, monto)
- El saldo deberá representar el dinero que tiene la otra persona
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente
”"""


class Persona:

    def __init__(self, nombre, edad, nacionalidad="Peruana"):
            self.nombre = nombre
            self.edad = edad
            self.nacionalidad = nacionalidad
            self.__saldo = 0

    def transferencia(self, persona2, monto):
            self.verificar_saldo()
            self.__saldo = self.__saldo + monto

    def verificar_saldo(self):
        if self.__saldo < 0:
            print("Saldo insuficiente")
            return
persona = Persona("Carlos", 28)
persona2 = Persona("Julio", 20)

persona.transferencia(persona2, 200)
