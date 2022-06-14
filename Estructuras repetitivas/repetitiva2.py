"""
Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. 
El ciclo debe finalizar cuando el usuario ingresa 0.
"""

numero = True

while numero != 0:
  numero = int(input("Si desea salir ingrese 0.\nIngrese un número: "))
  if numero % 2 == 0:
    print("Es par")
  else:
    print("Es impar")

print('El programa finalizo correctamente.')