from persona import Persona

class Masculino(Persona): 
    """Esta clase hereda de la super clase Persona,
    solo definiremos su constructor"""
  
    def __init__(self, nombre, edad, genero):
        self.nombre  = nombre
        self.edad = edad
        self.genero = genero
        print ("Hola señor "+nombre+" su edad es "+str(edad))