class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def estado(self):
        print("Arrancando: ", self.enmarcha)


class Motorizado(Vehiculo):

    def __init__(self, cadena, marca, modelo):
        super().__init__(marca, modelo)

        self.cadena = cadena

    def estado(self):
        super().estado()

        print("También: ", self.cadena)


# Esta sera la clase que hereda de Vehiculo
class Moto(Motorizado, Vehiculo):
    pass

mi_moto = Moto(marca="Toyota", modelo="Yaris", cadena="Trae cadena")
mi_moto.estado()