
#DESAFIO 2

"""
Realiza una función llamada relacion(a, b) que a partir de 
toneladas recicladas de dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.
"""

def relacion(a,b): # Pasa por valor en la definicion formal

  if n1>n2:
    ciudad = 'City 1'
  elif n1<n2:
    ciudad = 'City 2'
  elif n1 == n2:
    ciudad = 'City 1 y City 2'
  return ciudad

n1 = float(input('Ingrese la cantidad de toneladas de la ciudad 1: '))
n2 = float(input('Ingrese la cantidad de toneladas de la ciudad 2: '))
print(relacion(n1,n2)) # Pasa por valor en el actual al formal