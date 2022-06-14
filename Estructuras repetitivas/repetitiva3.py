"""
Calcular el monto a pagar por 
cada cliente y 
totalRecaudado recaudado

en una estación de servicio. 

Debe diseñar un programa que permita 
monto por cliente y 
el totalRecaudado recaudado por la gasolinera, 

tomando en cuenta lo siguiente:
• El precio del litro es para el 
A. $50
B. $55 
C. $60
D. Salir

"""

tipo = ''
tipoA = 50
tipoB = 55
tipoC = 60
totalRecaudado = 0

while tipo != 'D':
  print('###TIPOS DE GASOLINA###')
  print('Opcion A: 50$')
  print('Opcion B: 55$')
  print('Opcion C: 60$')
  print('Opcion D: Salir')
  
  monto = 0
  tipo = input('Ingrese el tipo de gasolina: ').upper()
  if tipo == 'A':
    litro = float(input('Ingrese la cantidad de litros: '))
    monto = litro * tipoA
    print(f'El monto total a pagar por el cliente es: {monto}')
  elif tipo == 'B':
    litro = float(input('Ingrese la cantidad de litros: '))
    monto = litro * tipoB
    print(f'El monto total a pagar por el cliente es: {monto}')
  elif tipo == 'C':
    litro = float(input('Ingrese la cantidad de litros: '))
    monto = litro * tipoC
    print(f'El monto total a pagar por el cliente es: {monto}')
  elif tipo == 'D': 
    print('¡Hasta luego, vuelva pronto!')
  else: print('Hubo un error')
  totalRecaudado += monto

print(f'totalRecaudado recaudado: {totalRecaudado}')
