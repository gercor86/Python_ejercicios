from femenino import Femenino
from masculino import Masculino

class Factoria(object):
    """Esta clase es nuestra factoria."""

    def get_persona(self, nombre, genero, edad):

    #genero es el parametro usado por la factoria 
    #para elegir el obj a crear
        if genero is 'F': 
            return Femenino(nombre, edad, genero)
        elif genero is 'M':
            return Masculino(nombre, edad, genero)