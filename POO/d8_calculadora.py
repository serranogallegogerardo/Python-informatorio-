# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora:
  def __init__(self, marca = '', a = 0, b = 0):
    self.marca = marca
    self.a = a
    self.b = b
  
  def __str__(self):
    return f'Soy la calculadora merca {self.marca}'
    
  def suma(self, a, b):
    return f'LA SUMA ES: {a + b}'

cal = Calculadora('Casio') #CREACION DEL OBJETO

print(cal.suma(6,8))

"""
class Calculadora:
  def __init__(self, marca):
    self.marca = marca

  def __str__(self):
    return f'Soy la calculadora merca {self.marca}'
    
  def suma (a, b):
    return a + b

print(Calculadora.suma(2,3))
"""
