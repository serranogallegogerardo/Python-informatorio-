# Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.

#la clase esta compuesta por atributos y metodos
#los atributos son sus cualidades nombre,colores,altura,ancho,etc...
#los metodos son ACCIONES que puede realizar dicho objeto
#que es un objeto? es el resultado de una clase.

class Persona: # Crear la clase
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def __str__(self):
    return f'PERSONA: {self.nombre} | EDAD: {self.edad}'

  def editar_nombre(self, nombre): # recibe el nombre "Carla"
    self.nombre = nombre # Edita el nombre

  def editar_edad(self, edad):
    self.edad = edad

  def es_mayor_de_edad(self):
    return self.edad >= 18 # Devuelve True o False

  def es_mayor_que(self, otra_persona):    
    return 'Si es Mayor' if self.edad > otra_persona.edad else 'La otra persona es Mayor'

  @staticmethod
  def obtener_el_mayor(obj1, obj2):
    if obj1.edad > obj2.edad:
      print(f'{obj1.nombre} es mayor edad.')
    elif obj1.edad < obj2.edad:
      print(f'{obj2.nombre} es mayor edad.')
    else:
      print('Los dos tienen la misma edad')

#objeto = clases(parametros)
Rolfi = Persona("Rodolfo", 42)
print(Rolfi)

Pablo = Persona('Pablo',30)
print(Pablo)

#Rolfi.editar_nombre("Carla")
#Rolfi.editar_edad(16)
print(f'Es mayor de edad: {Rolfi.es_mayor_de_edad()}')
Rolfi.es_mayor_de_edad()
print(Rolfi)

print(f'Nombre: {Rolfi.nombre}, Edad: {Rolfi.edad}')
#Rolfi.editar_edad(15)
print(Rolfi.es_mayor_que(Pablo))
# toma 2 argumentos posicionales pero 3 fueron dados
Persona.obtener_el_mayor(Rolfi, Pablo)
# Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.

"""
#Metodos privados
    def __enciendeLuzFreno(self):
        print("Luz del freno encendida")
    @staticmethod
    def corneta(precionar=False):
        if precionar==True:
            print("La corneta suena")
        else:
            print("La corneta no suena")
#Auto.corneta(True)
vocho1=Auto("1","rojo","2010","vocho")
vocho1.encender("1")
vocho1.corneta(True)
vocho1.apaga()

'''
Auto._alto=2
print(Auto._alto)
print(Auto._ancho)
print(Auto._velocidadMaxima)
vocho1=Auto("1","rojo","2010","vocho")
print(vocho1.color)
print(vocho1._alto)
"""