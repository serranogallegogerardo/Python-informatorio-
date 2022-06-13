# En un almacén se guarda mercadería en contenedores. 

"""
el contenedor maximo se puede apilar de a X en este caso (3) ingresando por el usuario

y maximo se puede tener 5 pilas de contenedores
c1  c1  c1  c1 c1  -> golosinas \
c2  c2  c2  c2 c2 -> gaseosas 
c3  c3  c3  c3 c3 -> limpieza 
resultado en codigo:
[[c1,c2,c3],[c1,c2,c3],[c1,c2,c3],[c1,c2,c3],[c1,c2,c3]]
"""

# No es posible colocar más de X(3) contenedores uno encima del otro y, no hay área para más de 5 pilas de contenedores. 

# Elabore un programa que permita gestionar el ingreso y salida 
#de contenedores. 

# Note que para retirar un container es necesario retirar los contenedores que están encima de él y colocarlos en otra pila.
"""
acciones de stack/pila

The functions associated with stack are:
FILO = first input/ last output
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

"""
import os

almacen = [[],[],[],[],[]]

def menu():
  print('Opciones del almacen:')
  print('1.Ingresar')
  print('2.Retirar')
  print('Otro.Salir')
  
x = int(input('Cuantos contenedores se pueden apilar?'))

def ingresarContenedor():
  print('Ha ingresado el contenedor')

def retirarContenedor():
  print('Ha retirado el contenedor')

# Note que para retirar un container es necesario retirar los contenedores que están encima de él y colocarlos en otra pila.

print('Bienvenido a almacen systems')
print('-sistema de gestion de stock-')
while True:
  menu()
  opcion = int(input('Elegir: '))

  if opcion == 1:
    ingresarContenedor()
  elif opcion == 2:
    retirarContenedor()
  else:
    break
  os.system('clear')
  
"""
#this is the first method.

replit. clear()
#this is the second method.
import os.
os. system('clear')
"""