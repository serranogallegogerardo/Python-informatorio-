"""
Se tiene una lista que almacena pedidos en orden de llegada,
por ende puede 
haber más de un pedido para el mismo artículo.
Crear una lista donde se almacene la 
cantidad de pedidos por artículo.
"""

cola = [["hamburguesa",4] , ["pizza",2] , ["empanadas",3], ['pizza',4]]

def menu():
  print("Delivery's System")
  print('1. Encargar Pizza')
  print('2. Encargar Hamburguesa')
  print('3. Encargar Empanadas')
  print('4. Ver pedido a entregar')
  print('5. Ver la cantidad de pedidos a hacer en total')
  print('6. Salir')

while True:
  menu()
  opcion = int(input('Elegir: '))
  if opcion == 1:
      cantidad = int(input('Cuantas pizzas quiere encargar?: '))
      cola.append(["pizza", cantidad])
      print(cola)
  elif opcion == 2:
      cantidad = int(input('Cuantas hamburguesas quiere encargar?: '))
      cola.append(["hamburguesa", cantidad])
      print(cola)
  elif opcion == 3:
      cantidad = int(input('Cuantas docenas de empanadas quiere encargar?: '))
      cola.append(["empanadas", cantidad])
      print(cola)
  elif opcion == 4:
    if len(cola) != 0:
      print(f'pedido a entregar {cola[0]}')
      print(cola.pop(0))
    else: print('No hay más pedidos.')
  elif opcion == 5:
    ac_h = 0
    ac_p = 0
    ac_e = 0
    for pedido, cantidad in cola:
      if pedido == 'hamburguesa':
        ac_h += cantidad
      elif pedido == 'pizza':
        ac_p += cantidad
      elif pedido == 'empanadas':
        ac_e += cantidad
    print('Cantidad de')
    print(f'Hamburguesas: {ac_h}')
    print(f'Pizzas: {ac_p}')
    print(f'Empanadas: {ac_e}')
  elif opcion == 6:
      break
