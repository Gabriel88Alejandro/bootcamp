

# comentario  de prueba para git
#print("prueba 16/07 ")
#print( " print de cambio")
class Persona:
    edad = 0
    def __init__(self, un_nombre):
        self.mi_nombre = un_nombre
        print("hola yo el nazi,  me llamo", self.mi_nombre)
    def cumple(self):
        self.edad = self.edad + 1
pepe = Persona("pepito")
pepa = Persona("pepita")
print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)
