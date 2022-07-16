#https://sites.google.com/view/informatorio-poo/level-silver/pr%C3%A9stamos?authuser=0

""" Se requiere un programa para registro de préstamos en una cooperativa. 



Los datos que se manejan para el préstamo son los siguientes:  
Número de Préstamo, 
Solicitante del préstamo. De quien se requiere únicamente: DNI, Primer Nombre, Primer y Segundo Apellido, teléfono de casa y teléfono móvil.  

Valor del préstamo
Fechas de pago de las cuotas (un máximo de 6 fechas, se asume que el plazo máximo de pago son 6 meses).  

Fecha de autorización del préstamo. 

 Fecha tentativa de entrega del préstamo. 

Las reglas que debe respetar este proyecto son las siguientes:  

El número de préstamo siempre deberá ser un valor mayor que cero.  

El valor del préstamo siempre debe ser mayor a cero.  

Se debe solicitar los datos de quien toma el préstamo.

La fecha tentativa de entrega del préstamo será siete días después de la fecha de autorización del préstamo.  

Las fechas de pago del préstamo se calculan, sumando 30 días a cada una a partir de la fecha de entrega del préstamo.  

Los préstamos solo se pueden autorizar en los primeros 20 días del mes. Esta es una política que nunca va a cambiar.

Además debes tener en cuenta que:

Existe una fecha máxima para la autorización de los préstamos. 

Existe un valor máximo a prestar. La sumatoria de los préstamos que se ingresen no debe exceder este valor.  

Debe permitir la carga de tantos préstamos como desee ingresar el usuario, a menos que se haya llegado al valor máximo a prestar.  

Debe imprimir los datos completos del préstamo, incluyendo la fecha de entrega y las fechas de pago de las cuotas. 

"""

import datetime

class Solicitantes:
  #DNI, Primer Nombre, Primer y Segundo Apellido, teléfono de casa y teléfono móvil.  
  def __init__(
              self,
              dni,
              nombre,
              apellido,
              telefonoCasa,
              telefonoMovil):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    self.telefonoCasa = telefonoCasa
    self.telefonoMovil = telefonoMovil


class Prestamos(Solicitantes):
  def __init__(
              self,
              numeroPrestamo,
              valorPrestamo,
              fechasPago,
              fechaAutorizacion,
              fechaEntrega,
              dni,nombre,apellido,telefonoCasa,telefonoMovil 
              ):
    super().__init__(dni,nombre,apellido,telefonoCasa,telefonoMovil)
    self.numeroPrestamo = numeroPrestamo
    self.valorPrestamo = valorPrestamo
    self.fechasPago = []
    self.fechaAutorizacion = fechaAutorizacion
    self.fechaEntrega = fechaEntrega

#fecha actual 11/07/2022
#fecha maxima 01/08/2022 agosto maximo
FechaMaxima = datetime.datetime(2022, 8, 1)
TenerEnCuenta = [FechaMaxima,200000]


"""
Además debes tener en cuenta que:

Debe permitir la carga de tantos préstamos como desee ingresar el usuario, a menos que se haya llegado al valor máximo a prestar.  

Debe imprimir los datos completos del préstamo, incluyendo la fecha de entrega y las fechas de pago de las cuotas
"""

#FECHAS 
#https://www.w3schools.com/python/python_datetime.asp