class Persona:
    @classmethod
    def saludar(cls, nombre):
        print('Saludando a: %s' %nombre)

Persona.saludar('Miguel')