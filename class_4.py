class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo= modelo
        self.enmarcha= False
        self.acelera = False
        self.frena= False
    
    def arrancar(self):
        self.enmarcha= True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
        
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando:", self.acelera, 
              "\nFrenando:", self.frena)

class Moto(Vehiculos):
    hwilly=""
    def willy(self):
        self.hwilly ="Voy haciendo willy por la avenida, delante de un camion."
    
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando:", self.acelera, 
              "\nFrenando:", self.frena, "\n", self.hwilly)

miMoto = Moto("Ghiggeri", "Vitta 110")

miMoto.willy()
miMoto.estado()