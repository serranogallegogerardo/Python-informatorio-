# Otra versión de lo mismo...
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def ver_color(self):
        print("El color del vehículo es {} ".format(self.color))
    
    def ver_ruedas(self):
        print("El vehículo tiene {} ruedas".format(self.ruedas))

class Coche (Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def ver_velocidad(self):
        print("La velocidad máxima del coche es {} ".format(self.velocidad))
    
    def ver_cilindrada(self):
        print("La cilindrada del coche es {} ".format(self.cilindrada))

color = input("ingrese el color del vehículo: \t")
ruedas = input("ingrese cantidad de ruedas del vehículo: \t")
velocidad = input("ingrese velocidad máxima del coche: \t")
cilindrada = input("ingrese cilindrada del coche: \t")

print ("")
print ("")

Auto = Coche(color,ruedas,velocidad,cilindrada)
Auto.ver_color()
Auto.ver_ruedas()
Auto.ver_velocidad()
Auto.ver_cilindrada()