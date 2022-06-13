

# Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. 
# El usuario llega y se ubica en la cola de menor cantidad de personas. 
# Al finalizar el proceso indique cuántos elementos tiene cada cola.

def colaLibre():
  print(len(cola1))
  print(len(cola2))

  if len(cola1) <= len(cola2):
      cola1.append(1)
      print('Entro a la cola 1')
  else:
      cola2.append(2)
      print('Entro a la cola 2')
    
cola1 = [1,1,1,1,1]
cola2 = [2,2,2]

print("Bienvenido a Rapipago")
print("Desea sacar turno ?")

while True:
  opcion = input("5.Entrar / 6.Irse: ")

  if opcion == "5":
    colaLibre()
  elif opcion == "6":
    break

  print("La cola se ve asi:")
  print(cola1)
  print(cola2)
  
