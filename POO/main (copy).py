# 6) Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:

  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
    self.aprobado = 'Ha aprobado' if nota > 4 else 'Ha desaprobado'
    
  def get_nota(self):

    if self.nota >=6:
      return 'aprobo'
    else:
      return 'desaprobo'

A1 = Alumno('Juan', 9)
A2 = Alumno('Pedro', 3)
A3 = Alumno('Esteban', 7)

print(A1.get_nota())
print(A2.get_nota())
print(A3.get_nota())
print(A1.aprobado)
print(A2.aprobado)
print(A3.aprobado)
