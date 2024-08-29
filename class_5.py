# nuevas clases

class Vehiculos():
    def __init__(self, marca, modelo):
        # marca es igual a la marca que le pasemos por paramotro
        self.marca=marca
        # modelo es igual a la modelo que le pasemos por paramotro
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
class Moto(Vehiculos):
    hwilly=""
    def willy(self):
        self.hcaballito="Voy haciendo willy, en la calle"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)
class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=600
    def cargarEnergia(self):
        self.cargando=True
    
miMoto=Moto("Giggheri", "Vitta 110")
miMoto.willy()
miMoto.estado()
class AutoElectrico(VElectricos,Vehiculos):
    pass
miAuto=AutoElectrico("Tesla", "BRC1944")
miAuto.estado()