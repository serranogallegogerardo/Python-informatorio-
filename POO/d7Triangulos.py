# Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

"""
El triángulo equilátero se caracteriza por tener todos sus lados iguales. El triángulo isósceles tiene dos lados iguales y un lado desigual. El triángulo escaleno tiene todos sus lados con diferentes longitudes.
"""

class Triangulo:

  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
    self.tipo = 'Isósceles' if self.a == self.b or self.b == self.c or self.c == self.a else 'Escaleno' if self.a != self.b and self.b != self.c and self.c != self.a else 'Equilátero'
    

  def __str__(self):
    return 'Soy un triangulo :D'

  def get_lado_mayor(self):
    if self.a >= self.b and self.a >= self.c:
      return self.a
    elif self.b >= self.a and self.b >= self.c:
      return self.b
    else:
      return self.c

  def get_tipo(self): # 1 1 1
    if self.a == self.b == self.c:
      return 'Equilátero'
    elif self.a == self.b or self.b == self.c or self.c == self.a == a:
      return 'Isósceles'
    else:
      return 'Escaleno'

f1 = Triangulo(3,4,5)
print(f1)
print(f1.get_tipo())
print(f1.get_lado_mayor())
