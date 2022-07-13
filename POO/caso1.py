"""
CASO1
A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos.

VEHICULO
  color
  ruedas

Coche 
  Velocidad 
  Cilindrada

"""

class VEHICULO:
  #atributos
  def __init__(self,color,ruedas):
    self.color = color
    self.ruedas = ruedas

  def __str__(self):
      return "Color {}, {} ruedas".format( self.color, self.ruedas )

class COCHE:
    def __init__(self,velocidad,cilindrada,color,ruedas):
      self.velocidad = velocidad
      self.cilindrada = cilindrada
      #Herencia
      self.color = color
      self.ruedas = ruedas
      self.vehicle()
      
      def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )
        
a = COCHE('27km/h',110,'Rojo','3')

print(a.color)
print(a