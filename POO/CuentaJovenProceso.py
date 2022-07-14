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
class CuentaElectronica:
  def __init__(self,titular,cantidad = 0): 
    self.titular = tiular
    self.cantidad = cantidad
    #metodos  
    def mostrar():
      print('Cuenta electronica')
      print('Titular {}'.format(self.titular))
      print('Cantidad {}'.format(self.cantidad))
    def ingresar(cantidad):
      if cantidad > 0:
        print('Cantidad {}'.format(self.cantidad))  
        self.cantidad += cantidad
    def retirar(cantidad):
        print('Cantidad {}'.format(self.cantidad))  
        self.cantidad -= cantidad
      
class CuentaJoven:
  def __init__(self,titular,cantidad,bonificacion ): 
    
    self.titular = tiular
    self.cantidad = cantidad
    
    
    """
    En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

Además la retirada de dinero sólo se podrá hacer si el titular es válido.

El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

 def esTitularValido():
    #true o false return

    def retirar(cantidad):
        print('Cantidad {}'.format(self.cantidad))  
        self.cantidad -= cantidad
      
    
    """

   
Cgera = CuentaJoven('Gerardo',100,30)