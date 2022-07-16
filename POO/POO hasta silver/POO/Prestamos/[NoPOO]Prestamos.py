#�#https://sites.google.com/view/informatorio-poo/level-silver/pr%C3%A9stamos?authuser=0

from datetime import datetime
from datetime import timedelta

import time
import os
import random

hoy = datetime.now()

def fecha(fecha):
  return f'{fecha.strftime("%d")}/{fecha.strftime("%m")}/{fecha.strftime("%Y")}'

class RegistrosDePrestamos:      
  def __init__(self,nombre):
    self.nombre = nombre
    self.montoTotal = 10000 # maximo que hay en el banco
    self.listaPrestamos = []

  def obtenerSolicitante(self):
    #dni,nombre,apellido,telefono,telefonoMovil
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

      print('Las fechas de pago son')
      print(fechasPago)
      
      fechaAutorizacion = hoy
      fechaTentativa = fechaAutorizacion + timedelta(days=7) 
      
      return {'numeroPrestamo': numeroPrestamo,'valorPrestamo' : valorPrestamo,'fechasPago' : fechasPago,'fechaAutorizacion' : fechaAutorizacion,'fechaEntrega' : fechaPago}
    else:
      print('los prestamos solo se otorgan del 1 al 20 del mes..')
      pass
      
    #print(fechasPago[])
    #dict = {}

    
class Prestamos():
  def __init__(
              self,
              numeroPrestamo,
              valorPrestamo,
              fechasPago,
              fechaAutorizacion,
              fechaEntrega
              ):
    #RegistrosDePrestamos().__init__(nombre)
    self.numeroPrestamo = numeroPrestamo
    self.valorPrestamo = valorPrestamo
    self.fechasPago = fechasPago
    self.fechaAutorizacion = fechaAutorizacion
    self.fechaEntrega = fechaEntrega
    

class Solicitantes(Prestamos):
  #DNI, Primer Nombre, Primer y Segundo Apellido, teléfono de casa y teléfono móvil.    
  def __init__(self,dni,nombre,apellido,telefonoCasa,telefonoMovil):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    self.telefonoCasa = telefonoCasa
    self.telefonoMovil = telefonoMovil
    self.fechaTentativa = fechaTentativa
    
    
    
    def PedirPrestamo(self):
      #sumar fechas con datetime.now() + timedelta(days=1)
      #dia de hoy
      
      #datos del solicitante en self
      if self.valorPrestamo > 0 and hoy.day <= 20 and self.valorPrestamo <= self.MontoTotal:
      #if dia in 1..20 and self.valorPrestamo > 0 and self.valorPrestamo < tenerEnCuenta[1]
        print('El monto actual disponible para prestar es de:', self.MontoTotal)
        self.valorPrestamo = self.MontoTotal - self.valorPrestamo
        print('Desea pagar en un solo pago o varios')
      #  self.fechaEntrega + 30d

      """
      xa = datetime.datetime.now()
      print(xa.day)
      """

    #ATRIBUTOS A TENER EN CUENTA POR LA CONSIGNA
    

############
#Debe imprimir los datos completos del préstamo, incluyendo la fecha de entrega y las fechas de pago de las cuotas. 
#############

cooperativa = RegistrosDePrestamos('Cooperativa Social')
numeroPrestamoN = 0


if __name__ == '__main__': # Si este programa se esta ejecutando como principal
  print('Bienvenido al programa de registro de prestamos')
  while True:
    #write your code here v:
    print("Que desea realizar ?\n")
    print('3. Pedir prestamo 💰')
    print('2. Saldo disponbile para prestamo: 💲   {}'.format(cooperativa.montoTotal) )
    print('1. Ver todos los prestamos 💹')
    print('Presione 0 para salir.')
    opcion = input('Opcion: ')
    if opcion == '1':
      pass
    elif opcion == '2':
      pass
    elif opcion == '3':
      numeroPrestamoN = 0
      #cooperativanombre, todoslosdatosdePrestamo
      print('Ingresando datos de solicitante....')
      
      # dni,nombre,blabalbala
      
      #datosSolicitante = cooperativa.obtenerSolicitante()
      datosPrestamo = cooperativa.obtenerPrestamo()
      
      
    elif opcion == '0':
      break
    
    os.system('clear')
   

#Registro
#Prestamos(Registro)
#Solicitante(Prestamos)