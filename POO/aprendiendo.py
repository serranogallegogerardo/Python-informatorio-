"""
CASO1
A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos.

VEHICULO
  color
  ruedas

Coche 
  Velocidad 
  Cilindrada


Seres vivos
  Humanos
    Cualidades(Atributos)
    Acciones(Metodos)

Hacer una maquina expendedora
Maquina
  Bebida

Machineitor4000 = Maquina('Machineitor4000','rojo','Cocacola')


Maquina
  #atributos
  self.nombre =
  self.color = 
  self.stickers =
  #metodos
  def comprarbebida()
  def cargarbebidas()

  Bebidas
    self.estado = ('frio','caliente')
    self.color = 'rojo'

"""

class VEHICULO:
  #atributos/cualidades
  def __init__(self,color,ruedas,motor):
    self.color = color
    self.ruedas = ruedas
    self.motor = motor
  #ACCIONES METODOS
  def __str__(self):
      return('Soy parte del molde y tengo estas cualidades: {}\n {}'.format(self.color,self.ruedas))

  def Arrancar(self):
    print('Enciendo vehiculo...!!')
    print('Vehiculo Encedido color {}'.format(self.color))
  def Apagar(self):
    print('Apagando vehiculo.. {}'.format(self.color))


Moto = VEHICULO('Blanco',4)
Cuatri = VEHICULO('AZUL', 6)
Bichonuevo = VEHICULO('Violeta',9)

Moto.Apagar()
Bichonuevo.Arrancar()
print(Cuatri.color)
print(Bichonuevo.ruedas)

#a = COCHE('27km/h',110,'Rojo','3')



"""

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
"""