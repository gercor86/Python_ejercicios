import math

class Vector:
    def __init__ (self,px=0, py=0):
        self.x = px
        self.y = py
    
    def __str__(self):
        return ("%f,%f") % (self.x, self.y)
    
# Sobre cargando funciones.

    def __add__(self, operando):    
            mx = self.x + operando.x
            my = self.y + operando.y
            
            return Vector(mx, my)
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, operando):
        return self.magnitud() == operando.magnitud()
    
    def __gt__(self, operando):
        return self.magnitud()>operando.magnitud()

a = Vector(4, 4)

b = Vector(-8, 8)

print(a)

print(b)

c = a + b

print(c)

print(a.magnitud())

if(a==b):
   print("a y b son iguales")
else:
   print("a y b no son iguales")

if(a==c):
   print("a y b son iguales")
else:
   print("a y b no son iguales")

if(a>b):
   print("a es mayor")
else:
   print("b es mayor")