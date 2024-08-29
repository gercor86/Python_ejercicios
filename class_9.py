# Clases

class Humano:
    
    def __init__(self):
        self.nombre = "Gordon"
        self.traje = self.Traje()
        self.palanca = self.Palanca()
    
    class Traje:
        def usar(self):
            return "Todos los sistemas del traje activados."
        
    class Palanca:
        def usar(self):
            return "Golpeando con la palanca objetos."
    
if __name__ == "__main__":
    gordon = Humano()
    
print(gordon.nombre)
print(gordon.traje.usar())
print(gordon.palanca.usar())