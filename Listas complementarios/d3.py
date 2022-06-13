# Realizar un algoritmo que invierta el orden de una cola.

lista = [1,2,3,4,5,6,7,8,9]
nueva_lista = []
for i in reversed(lista):
    nueva_lista.append(i)
print(nueva_lista)

frutas = ['banana','manzana','naranja']
frutas.reverse()
print(frutas)