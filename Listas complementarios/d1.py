#	Cargar m elementos en una pila, y luego copiarlos en una nueva lista.
# Cargar k elementos en una cola, y luego copiarlos en una nueva lista.

pila = []
newlist = []

while True:

  elemento = int(input('Ingrese el elemento para apilar: '))
  pila.append(elemento)
  print(f'La pila se ve asi: {pila}')
  
  if input('¿Desea continuar? (si/no): ') == 'no':
    print('Hasta luego!')
    break

newlist = pila.copy()
print(f'La pila copiada es :{newlist}')
