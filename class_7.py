class Coche():
    def desplamiento(self):
        print("Me muevo con 4 ruedas.")

class Moto():
    def desplazamiento(self):
        print("Me muevon con 2 ruedas.")

class Camion():
    def desplazamiento(self):
        print("Me muevo con muchas ruedas y un acoplado.")


def desplamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
miVehiculo = Moto()
    
desplamientoVehiculo(miVehiculo)