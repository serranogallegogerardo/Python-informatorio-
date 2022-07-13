"""
CASO1
A partir del siguiente diagrama de clases, 


VEHICULO
  color
  ruedas

Coche 
  Velocidad 
  Cilindrada


Seres vivos
  estado = 0,1
  tipo = ('')

  def vivir()
    return 'estoy viviendo'

  Humanos
    altura = 2
    nombre = ''

    Deportistas

      Gymnastas
        entrenamiento = 123
        
      Crossfitero
        entrenamientoFuncional = abc
  
      Calistenico
        entrenamientoTorso = xyz
"""


class VEHICULO():
  def __init__(self, color, ruedas):
    self.color = color
    self.ruedas = ruedas

  def chocar(self):
    print('chocó...')
    self.ruedas -= 1
    print('Pierde una rueda le quedan: {}'.format(self.ruedas))

class MOTO(VEHICULO):
  def __init__(self, color, ruedas, velocidad, cilindrada):
    super().__init__(color, ruedas)
    #NUEVOS ATRIBUTOS DE LA MOTO
    self.velocidad = velocidad
    self.cilindrada = cilindrada

  def hacerwily(self):
    print('!!! ESTOY HACIENDO WILI RUM RUM !!!')
    
XTZ = MOTO('Rojo',4, 100, 250)
XTZ.hacerwily()
XTZ.chocar()
auto = VEHICULO('negro', 5)
auto.chocar()
auto.hacerwily()

"""

HERENCIA
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

auto = VEHICULO('Rojo',4)
moto = VEHICULO("azul",2)
cuatri = VEHICULO('negro', 6)

auto.chocar()
moto.chocar()

cadena = moto.chocar()
print(cadena)

"""