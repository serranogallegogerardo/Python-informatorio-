"""
Determinar el número mayor de 10 números ingresados.
-busco el numero mas grande 
"""

mayor = 0

for i in range(10): #range (inicio, fin, paso)
  numeroActual = int(input(f'Ingrese un número {i+1}: '))
  if numeroActual > mayor:
    mayor = numeroActual

print(f'El numero mayor es {mayor}')
