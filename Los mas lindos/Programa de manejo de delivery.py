#MEJOR COD

# Se tiene una lista que almacena pedidos en orden de llegada, 
# por ende puede haber más de un pedido para el mismo artículo. 
# Crear una lista donde se almacene la cantidad de pedidos por artículo.

import os
import time

cola = [["hamburguesa","4"] , ["pizza","2"] , ["empanadas","3"], ['pizza',"4"]]

def menu():
  print("Delivery's System")
  print('1. Encargar Pizza')
  print('2. Encargar Hamburguesa')
  print('3. Encargar Empanadas')
  print('4. Entregar Primer Pedido')
  print('5. Ver la cantidad de pedidos a hacer en total')
  print('6. Salir')

def mostrar():
  cont = 1
  os.system('clear')
  print('--- --- ---'.center(50, "*"))
  for pedido, cantidad in cola:
    print(f'-Pedido {cont} es {pedido}, cantidad: {cantidad}.')
    cont+=1
  print('--- --- ---'.center(50, "*"))

def Mensaje(mensaje):
  os.system('clear')
  print('--- --- ---'.center(50, "*"))
  print(mensaje)
  print('--- --- ---'.center(50, "*"))
  time.sleep(2.0)

while True:
  mostrar()
  menu()
  try:
    opcion = int(input('Elegir: '))
    if opcion == 1:
        cantidad = input('Cuantas pizzas quiere encargar?: ')
        cola.append(["pizza", cantidad])
        #mostrar()
    elif opcion == 2:
        cantidad = input('Cuantas hamburguesas quiere encargar?: ')
        cola.append(["hamburguesa", cantidad])
        #mostrar()
    elif opcion == 3:
        cantidad =input('Cuantas docenas de empanadas quiere encargar?: ')
        cola.append(["empanadas", cantidad])
        #mostrar()
    elif opcion == 4:
      try:
        cad = ", ".join(cola[0])
        #print(f'Pedido a entregar {cad}')
        Mensaje(f'Pedido a entregar {cad}')
        cola.pop(0)
      except IndexError: 
        Mensaje('No hay más pedidos.')
    elif opcion == 5:
      ac_h = 0
      ac_p = 0
      ac_e = 0
      for pedido, cantidad in cola:
        cantidad = int(cantidad)
        if pedido == 'hamburguesa':
          ac_h += cantidad
        elif pedido == 'pizza':
          ac_p += cantidad
        elif pedido == 'empanadas':
          ac_e += cantidad
      os.system('clear')
      print('--- --- ---'.center(50, "*"))
      print('Cantidad Total de Pedidos a Entregar:')
      print(f'Hamburguesas: {ac_h}')
      print(f'Pizzas: {ac_p}')
      print(f'Empanadas: {ac_e}')
      print('--- --- ---'.center(50, "*"))
    elif opcion == 6:
        break
    else:
      Mensaje('Solo se admite opciones del 1-6.')
  except ValueError:
    Mensaje('Solo se admiten valores númericos')


