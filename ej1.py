# Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.

#temas
#Constructores en python
#self

class Persona:
  #declaracion de clase con sus atributos
      #constructor __init__
  def __init__(self, nombre, edad):
    #atributo de este objeto le asigno = ...
    # atributo = valor
    self.nombre = nombre
    self.edad = edad

  def __str__(self):
    return f'Nombre: {self.nombre} | Edad: {self.edad}'
  
  def set_edad(self, edad):
    self.edad = edad

  def set_nombre(self, nombre):
    self.nombre = nombre

#Creacion de objeto en python
Player1 = Persona("Carlos", 38)
print(Player1)

Player1.set_edad(18)
print(Player1)

#objetonombre = clase(parametros)
Player2 = Persona("Rodollfo", 23)
print('Rodolfo esta siendo modificado..')
print('Rodolfo tenia:')
print(Player2.nombre)
print(Player2.edad)
print('After modifikeishon')
print(Player2.set_edad(25))

print(Player2.edad)