
class Dino:
    def __init__(self,un_nombre, un_color, un_gusto, canti_patas=2, un_genero=None):
        self.nombre= un_nombre
        self.color= un_color
        self.gusto= un_gusto
        self.patas= canti_patas
        self.genero= un_genero
        print("acabo de nacer mira abajo")
        print()
        print("si aca abajo")
        print()
    def saludar(self):
        print(" mi nombre es", self.nombre, "soy de color ", self.color, " y me gusta la ", self.gusto, "tengo, ", self.patas, "patas", "y soy", self.genero)
crispulo = Dino("crispulito,","marron", "carne", 2, "super macho") 
crispulo.saludar()     # las acciones (metodos) son indicadas con parentecis al final, se llam a la funcion o atributo o lo que sea con un "." 