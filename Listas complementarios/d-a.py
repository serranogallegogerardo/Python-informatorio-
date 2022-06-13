"""
a. Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
# ana oso 
"""

cad = []

while True:
  car = input("Ingrese la palabra letra por letra: ")
  cad.append(car)

  if input("Ingrese Otro.Si - 1.No: ") == "1":
    print("Gracias por utilizar el programa")
    break

print(cad[0:])
print(cad[::-1])

if cad == cad[::-1]:
    print('La cadena es palíndromo')
else:
    print('La cadena no es palíndromo')