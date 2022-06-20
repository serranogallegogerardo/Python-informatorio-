"""

Ejercicio 13: Contraseña aleatoria

-Escriba una función que genere una contraseña aleatoria. 

-De longitud aleatoria de entre 7 y 10 caracteres. 

-Cada carácter debe seleccionarse al azar de las posiciones 33 a 126 en la tabla ASCII.

-Su función no tomará ningún parámetro y devolverá la contraseña generada aleatoriamente como su único resultado.

-Desarrolle un programa principal y muestre la contraseña generada aleatoriamente.

"""

print('Bienvenido a contraseña random')


#-Cada carácter debe seleccionarse al azar de las posiciones 33 a 126 en la tabla ASCII.
# 33 a 126
#>'!' and <= '}'
#https://elcodigoascii.com.ar/codigo-americano-estandar-intercambio-informacion/codigo-ascii.png

import random
# 33 - 47 = carácteres especiales
# 48 - 57 = números
# 58 - 64 = carácteres especiales 2
#easy jajajja ! hasta ~
print(chr(random.randint(33,126)))
#ord()


def randContrasena():

  x = ''
  for i in range(random.randint(7,10)):
    #funcion random.randint()
      x = x + chr(random.randint(33,126))

  return x

print(randContrasena())

"""

def randContrasena():

  x = 1
  while x < random.randint(7,10):
    #funcion random.randint()
    if (>'!' and <= '}'):
      random.randint('!','}')
      x += 1

number_of_strings = 5
length_of_string = 8
for x in range(number_of_strings):
  print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

La función random.randint() 
se puede utilizar para devolver un número aleatorio dentro de un rango específico; el programador puede especificar el rango. La función random.randint() está contenida en el módulo incorporado random proporcionado por Python, que debe importarse al código Python para poder utilizar esta función.

La función random.randint() es un alias para la función random.randrange() y contiene dos parámetros obligatorios: start y stop. Estos parámetros especifican el rango entre el que queremos generar un número aleatorio o una letra.

Para generar una letra aleatoria en Python, se puede implementar la misma función random.randint().

El siguiente código usa la función random.randint() para generar una letra aleatoria en Python.


"""