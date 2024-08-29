class Coche():
    def dezplazamiento(self):
        print("Me muevo con 4 ruedas.")
        
class Moto():
    def dezplazamiento(self):
        print("Me muevo solo con 2 ruedas.")

class Camion():
    def dezplazamiento(self):
        print("Me muevon con muchas ruedas y acomplados.")

miVehiculo =Moto()

miVehiculo.dezplazamiento()

miVehiculo2 =Coche()

miVehiculo2.dezplazamiento()

miVehiculo3 =Camion()

miVehiculo3.dezplazamiento()