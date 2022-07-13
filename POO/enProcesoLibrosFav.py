



"""
MIS LIBROS FAVS
Vamos a crear un programa para nuestros libros favoritos, así leemos un poco más.

Queremos mantener una lista de los libros que hemos ido leyendo, calificando según nos haya gustado más o menos al leerlo. 

Para ello, crear la clase Libro, cuyos atributos son el titulo, el autor, el número de páginas y la calificación que le damos entre 0 y 10. 

Crear los métodos para poder modificar y obtener los atributos si tienen sentido. 

Posteriormente, crear una clase ConjuntoLibros,
que almacena un conjunto de libros.
Se pueden añadir libros que no existan (siempre que haya espacio),
eliminar libros por título o autor, 
mostrar por pantalla los libros con la 
mayor y menor calificación dada y,
por último, mostrar un contenido de todo el conjunto. 
"""

# ConjuntoLibros
class Libro:
  def __init__(self, titulo, autor, nroPaginas, calificacion):
    self.titulo = titulo
    self.autor = autor
    self.nroPaginas = nroPaginas
    self.calificacion = calificacion
    for k, v in vars(self).items():
      print('{}: {}'.format(k.capitalize(),v), end=' | ')
    print('\n')

  def __str__(self):
    return 'Soy el objeto libro'
    
  def get_atributos(self):
    return vars(self)
  
  def modificar(self,titulo, autor, nroPaginas, calificacion):
    self.titulo = titulo
    self.autor = autor
    self.nroPaginas = nroPaginas
    self.calificacion = calificacion
    print('\n')
    print('Usted modificó: ', end='')
    #print(vars(self))
    for k, v in vars(self).items():
      print('{}: {}'.format(k.capitalize(),v), end=' | ')
      

class ConjuntoLibros:
  def __init__(self,cantidadMaxima):
    self.cantidadMaxima = cantidadMaxima
    self.contenedor = []
    
  #quedaria llena al estar asi:
  #self.contenedor = [libro,libro,libro,libro,libro]
    
  def agregar(self, titulo, autor, nroPaginas, calificacion):
    
    if len(self.contenedor) < self.cantidadMaxima:
      libro = Libro(titulo, autor, nroPaginas, calificacion)
      if libro not in self.contenedor:
        #print(libro)
        self.contenedor.append(libro)
    else:
      print('El conjunto de libros esta lleno.')


#eliminar libros por título o autor, 
  def eliminar (self, titulo = '', autor = ''):
    for libro in self.contenedor:
      if libro.titulo == titulo or libro.autor == autor:
        index = self.contenedor.index(libro)
        print(f'Se borró el libro: {libro.titulo}')
        self.contenedor.pop(index)
        return 0
    print("No existe el titulo/autor indicado")

  def mostrar(self):
    for libro in self.contenedor:
      for k, v in vars(libro).items():
        print('{}: {}'.format(k.capitalize(),v), end=' | ')
      print('\n')
        
     




# print(SrAnillos.get_atributos())

libro1 = Libro('Como ser tu propio jefe','Roberto Venegas',200,6.3)
libro2 = Libro('El camino de dios','Roberto Venegas',200,2.3)

biblioteca = ConjuntoLibros(5)

biblioteca.agregar('SrAnillos 2010','Roberto Venegas',200,7.3)
biblioteca.agregar('Awantiaaa','Eldevamo Niubel',30,10)

biblioteca.contenedor.append(libro1)
biblioteca.contenedor.append(libro2)

biblioteca.eliminar('Awantiaaa')
print('\n***************************************************\n')
biblioteca.mostrar()