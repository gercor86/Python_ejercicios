class Coche():
    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False
    #definir metodo
    def arrancar(self,arrancamos):
        #definir comportamiento
        self.enmarcha=arrancamos
        if (self.enmarcha):
           return "El coche esta en marcha"
        else:
           return "El coche esta detenido"
    #definir metodo
    def estado(self):
        #definir comportamiento
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un larde de ", self.largoChasis)
    
#definir objeto y a que clase pertenece
miChoche=Coche() 
print(miChoche.arrancar(True))
miChoche.estado()