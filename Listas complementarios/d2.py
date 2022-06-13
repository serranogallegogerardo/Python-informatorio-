# Construya un algoritmo que sume todos los elementos en posición par de una lista 

pila = []
newlist = []

while True:

  elemento = int(input('Ingrese el elemento para apilar: '))
  pila.append(elemento)
  print(f'La pila se ve asi: {pila}')
  
  if input('¿Desea continuar? (si/no): ') == 'no':
    print('Hasta luego!')
    break

#para practicar la filosofia de cola
newlist = list(pila)
#newlist = pila.copy()
print(f'La pila copiada es :{newlist}')
