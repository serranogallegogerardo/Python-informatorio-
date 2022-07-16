"""

Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.  

#

Implementa los siguientes métodos:
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de lo que definas al resolver el problema Cuenta Electrónica. 

Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
Construye los siguientes métodos para la clase:

En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

Además la retirada de dinero sólo se podrá hacer si el titular es válido.

El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
"""
class Cuentaelectronica:
  def __init__(self,titular,cantidad = 0): 
    self.titular = titular
    self.cantidad = cantidad
    #metodos  
  def mostrar(self):
    print('Cuenta electronica')
    print('Titular {}'.format(self.titular))
    print('Cantidad {}'.format(self.cantidad))
      
  def ingresar(self,cantidad):
    if cantidad > 0:
      print('Cantidad old {}'.format(self.cantidad))  
      self.cantidad += cantidad
      print('Cantidad new {}'.format(self.cantidad))  
  def retirar(self,cantidad):
      print('Cantidad old {}'.format(self.cantidad))  
      self.cantidad -= cantidad
      print('Cantidad new {}'.format(self.cantidad)) 
      
      
class CuentaJoven(Cuentaelectronica):
  def __init__(self,titular,cantidad,bonificacion, edad):
    super().__init__(titular,cantidad)
    self.bonificacion = bonificacion
    self.edad = edad
    
  def esTitularValido(self):
    if self.edad > 18 and self.edad < 25:
      return True
    else:
      return False

  def retirar(self,cantidad = 0):
    if self.edad > 18 and self.edad < 25:
      mayorDeEdad = True
    else:
      mayorDeEdad = False
    
    if mayorDeEdad and cantidad != 0:
      print('Cantidad old {}'.format(self.cantidad))  
      self.cantidad -= cantidad
      print('Cantidad new {}'.format(self.cantidad))
    elif cantidad == 0 or mayorDeEdad == False:
      print('Error no puede retirar dinero')

  def mostrar(self):
    print('Cuenta Joven')
    print('Titular {}'.format(self.titular))
    print('Cantidad {}'.format(self.cantidad))
    print('Bonificacion: {}%'.format(self.bonificacion))
        
uala = Cuentaelectronica('Pierpaolo Barbieri',32000)

#uala.ingresar(100)
#uala.retirar(10000)
#uala.mostrar()

BCHACO = CuentaJoven('RodolfoVargas',100,30,23)

#BCHACO.retirar()
#BCHACO.mostrar()

for key,value in vars(BCHACO).items():
  print('{} - {}'.format(key,value))
print(type(BCHACO).__name__)