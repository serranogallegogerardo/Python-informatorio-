"""
https://sites.google.com/view/informatorio-poo/level-stone?authuser=0
Caso 2 
Mis Libros Favs
Barajas
Tenis

Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.

Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""
# CASO 2
# funciones
"""
Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""

def mostrar(Vehiculos):
    for vehiculo in Vehiculos:
        print(vehiculo)\

def catalogar(Vehiculos, ruedas = 0):
  count = 0
  for vehiculo in Vehiculos:
    if ruedas == vehiculo.ruedas:
        print(type(vehiculo).__name__)
        for k, v in vars(vehiculo).items():
          print('{}: {}'.format(k.capitalize(),v), end=' | ')
        count +=1
        print('\n')
  if ruedas > 0:
    print('Se han encontrado {} con {} ruedas'.format(count,ruedas))
  elif count == 0:
    print('\033[0;31mNo pusiste la cantidad de ruedas.\033[0m')

"""
  print('\033[0;31mNo se encontró con esa cantidad de ruedas.\033[0m')
      elif 
        break
"""
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):  # Coche -> Vehiculo
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Coche):  # Camioneta -> Coche -> Vehiculo
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

# Herencias segunda rama

class Bicicleta(Vehiculo):  # Bicicleta -> Vehiculo
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):  # Motocicleta -> Bicicleta -> Vehiculo
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

Vehiculos = []
XTZ = Motocicleta('Azul', 2, 'Street', '114km/h', 110)
Vehiculos.append(XTZ)
AHD = Motocicleta('Azul', 1, 'Street', '125km/h', 110)
Vehiculos.append(AHD)
fiat = Vehiculo('Blanco', 4)
Vehiculos.append(fiat)
renault = Camioneta("Negro", 4, 230,110,300)
Vehiculos.append(renault)

catalogar(Vehiculos, 2)
