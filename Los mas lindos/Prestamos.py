#�#https://sites.google.com/view/informatorio-poo/level-silver/pr%C3%A9stamos?authuser=0

from datetime import datetime
from datetime import timedelta
import time
import os
import random

hoy = datetime.now()

"""
class Solicitantes(): 
  def __init__(self,dni,nombre,apellido,telefonoCasa,telefonoMovil,fechaTentativa):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    self.telefonoCasa = telefonoCasa
    self.telefonoMovil = telefonoMovil
    self.fechaTentativa = fechaTentativa
    
preferi usar como un dict esto...
"""

class Prestamos():
  def __init__(
              self,
              numeroPrestamo,
              solicitante,
              valorPrestamo,
              fechasPago,
              fechaAutorizacion,
              fechaTentativa
              ):
    self.numeroPrestamo = numeroPrestamo
    self.solicitante = solicitante
    self.valorPrestamo = valorPrestamo
    self.fechasPago = fechasPago
    self.fechaAutorizacion = fechaAutorizacion
    self.fechaTentativa = fechaTentativa

class RegistrosDePrestamos:      
  def __init__(self,nombre):
    self.nombre = nombre
    self.montoTotal = 10000 # maximo que hay en el banco para prestar
    self.listaPrestamos = []

  def obtenerSolicitante(self):
    dni = int(input('Ingrese su dni: '))
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    telefono = input('Ingrese su telefono: ')
    telefonoMovil = input('Ingrese su telefonoMovil: ')
    return { 'dni':dni , 'nombre': nombre, 'apellido':apellido, 'telefono': telefono, 'telefonoMovil' : telefonoMovil }

  def obtenerPrestamo(self):
    
    if hoy.day <= 20:
      print('Permiso concedido..')
      numeroPrestamo = random.randint(0,99)
      
      while True:
        valorPrestamo = int(input('Ingrese el valor del prestamo: '))
        if valorPrestamo <= self.montoTotal or valorPrestamo == 0:
          self.montoTotal -= valorPrestamo
          break
        else:
          print('error, no se puede prestar esa cantidad \n 0. Salir')

      while True:
        fechasPagoX = int(input('en cuantas cuotas desea realizar el pago\n (solo de 1 hasta 6): '))
        if fechasPagoX in range(1,7):
          break
        else:
          print('error ingrese nuevamente')

      fechasPago = []
      dia = 30
      for i in range(0,fechasPagoX):
        fechasPago.append((hoy+timedelta(days=dia)))
        dia+=30

      fechaAutorizacion = hoy
      fechaTentativa = fechaAutorizacion + timedelta(days=7) 
      
      return {'numeroPrestamo': numeroPrestamo,'valorPrestamo' : valorPrestamo,'fechasPago' : fechasPago,'fechaAutorizacion' : fechaAutorizacion,'fechaTentiva' : fechasPago}
    else:
      print('los prestamos solo se otorgan del 1 al 20 del mes..')
      pass
    

##CODIGO PRINCIPAL######################################################################

cooperativa = RegistrosDePrestamos('Cooperativa Social')

if __name__ == '__main__': # Si este programa se esta ejecutando como principal
  
  print('Bienvenido al programa de registro de prestamos')
  while True:

    print("Que desea realizar ?")
    print('Saldo disponbile para prestamo: 💲   {}'.format(cooperativa.montoTotal) )
    print('2. Pedir prestamo 💰')
    print('1. Ver todos los prestamos 💹')
    print('Presione 0 para salir.')
    opcion = input('Opcion: ')
    
    if opcion == '2':

      os.system('clear')
      
      print('Ingresando datos de solicitante....')
      ### ACA ESTA EL DATO
      datosSolicitante = cooperativa.obtenerSolicitante()
      datosPrestamo = cooperativa.obtenerPrestamo()

      prestamo = Prestamos(datosPrestamo['numeroPrestamo'],
                           datosSolicitante,
                           datosPrestamo['valorPrestamo'],
                           datosPrestamo['fechasPago'],
                           datosPrestamo['fechaAutorizacion'],
                           datosPrestamo['fechaTentiva'])

      print('')
      for key,value in vars(prestamo).items():
        print('{} : {}'.format(key,value))

      cooperativa.listaPrestamos.append(prestamo)
      

      
        
      #numeroPrestamo,
      #solicitante, # es un dict xd
      #valorPrestamo,
      #fechasPago, # es una lista de objetos donde cada objeto es una fecha
      #fechaAutorizacion,
      #fechaTentativa
      
      #for key,value in datosSolicitante.items():
      #  print('{} : {}'.format(key,value))

      
      
      #time.sleep(15)
      
    elif opcion == '1':
      print('')
      for i in cooperativa.listaPrestamos:
        print(vars(i))
        print('')
      
      time.sleep(15)
    elif opcion == '0':
      break
    os.system('clear')

#Tiene bugs irrelevantes y solucionables obviamente pero lo dejo hasta aca porque ya le meti muchas horas.. y debo seguir con los siguientes..

#Registro
#Prestamos(Registro)
#Solicitante(Prestamos)

############
#Debe imprimir los datos completos del préstamo, incluyendo la fecha de entrega y las fechas de pago de las cuotas. 
#############
