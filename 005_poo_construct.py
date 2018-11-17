class Coche():

    def __init__(self):
        self.largo_chasis = 250
        self.ancho_chasis = 120

        # Encapsulamiento, es decir no es accesible fuera de la clase. No se puede modificar desde fuera de la clase.
        self.__ruedas = 4

        self.en_marcha = False

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = True
        self.aceite = True
        self.puertas = True

        if self.gasolina and self.aceite and self.puertas:
            return True
        else:
            return False

    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos

        if self.__en_marcha:
            chequeo = self.__chequeo_interno()

            if chequeo:
                return ("El coche está en marcha")
            else:
                return "Algo ha ido mal en el chequeo, no se puede arrancar"
        else:
            return ("El coche está parado")

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.ancho_chasis)

mi_coche = Coche()
print(mi_coche.arrancar(True))
mi_coche.estado()