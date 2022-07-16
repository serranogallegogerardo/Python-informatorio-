#G9 CAFE
"""
#CAFE
https://sites.google.com/view/informatorio-poo/level-stone/level-stone?authuser=0#h.aq5rs2uakg5d

Desarrolla una clase Cafetera con atributos _capacidadMaxima (la cantidad máxima de café que puede contener la cafetera) y _cantidadActual (la cantidad actual de café que hay en la cafetera). 

Luego desarrollar los siguientes métodos:

llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la capacidad.  

servirTaza(int): simula la acción de servir una taza con la capacidad indicada. Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que quede.  

vaciarCafetera(): pone la cantidad de café actual en cero.  

agregarCafe(int): añade a la cafetera la cantidad de café indicada.

Cómo quedaría ese programa? Probalo.
"""


class CAFETERA:
  def __init__(self,_capacidadMaxima,_cantidadActual):
    self._capacidadMaxima = _capacidadMaxima
    self._cantidadActual = _cantidadActual
    self._falta = _capacidadMaxima - _cantidadActual
  #atributos
  
  #metodos

  """
class TAZA:
  def __init__(self,_capacidadMaxima,_cantidadActual):
    self._capacidadMaxima = _capacidadMaxima
    self._cantidadActual = _capacidadActual
    
  
  llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la capacidad.  

servirTaza(int): simula la acción de servir una taza con la capacidad indicada. Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que quede.  

vaciarCafetera(): pone la cantidad de café actual en cero.  

agregarCafe(int): añade a la cafetera la cantidad de café indicada.

Cómo quedaría ese programa? Probalo.
  """

  def __str__():
      return 'Soy una cafetera BF BFFFFFFFFF'
  def llenarCafetera(self):
    self._cantidadActual = self._capacidadMaxima

  def get_servirTaza(self,capacidadTaza = 250):
    if (self._cantidadActual < capacidadTaza):
      self._cantidadActual = 0
      print('No alcanza para llenar, se sirve lo que quedo')
    else:
      self._cantidadActual = self._cantidadActual - capacidadTaza
      print('Si alcanza lo que queda para llenar.')
   
  def get_vaciarCafetera(self):
    self._cantidadActual = 0
    print( 'Cafetera vaciada...' )

  #objeto.agregarcafe(140)
  def agregarCafe(self,carga = -1):
    #max - actual = falta 
    # ta de mas
    #self.falta = self._capacidadMaxima - self._cantidadActual
    
    if carga > 0 and carga <= (self._capacidadMaxima-self._cantidadActual): # no sobrepasa
      self._cantidadActual += carga
      print('Ahora tenes cargado : {}'.format(self._cantidadActual))
    elif carga == -1:
      print('Falta agregar la carga en mililitros')
    else: # sobrepasa
      print('No se puede sobrepasar la capacidad {}ml maxima de la cafetera. '.format(self._capacidadMaxima))      

CDOLCA = CAFETERA(1000,600)
CDOLCA.get_vaciarCafetera()
CDOLCA.agregarCafe(200)
CDOLCA.get_servirTaza()
CDOLCA.llenarCafetera()
print(CDOLCA._cantidadActual)

