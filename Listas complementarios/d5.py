# Escriba un algoritmo que permita cargar una lista.
# Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.
lista = []

while True:
  elemento = int(input('Ingrese el elemento para enlistar: '))
  lista.append(elemento)
  print(f'La lista se ve asi: {lista}')
  if input('¿Desea continuar? (si/no): ') == 'no':
    print('Hasta luego!')
    break

# Forma directa x elemento
for i in lista:
    if i < 0: #
        #lista[i] = 0
        lista[lista.index(i)] = 0
print(f'La lista final es: {lista}')

# 2da forma mas tradicional
for i in range(0,len(lista),1):
    if lista[i] < 0:
        lista[i] = 0
print(f'La lista final es: {lista}')
