

lista_total = []
lista_menos100 = []
lista_mas100 = []

def separar(lista):
  for i in lista: # [1,32,3,2,32,32,3,]
      if i > 100: 
        lista_mas100.append(i)
        print('La cantidad de ciudades >100 es de :', len(lista_mas100))
        sorted(lista_mas100)
        
      elif i <= 100:
        lista_menos100.append(i)
        sorted(lista_menos100)

  return lista_menos100 # falta la otra lista retornar con .extend o algo
 # return lista_mas100


#MAIN!!!
q_ciudades = int(input("Ingrese la cantidad de ciudades a analizar: "))

while q_ciudades != 0:
    lista_total.append(int(input('¿Cuantos arboles plantó la ciudad?: ')))
    #lista_total.sorted
    q_ciudades -= 1
    

separar(lista_total)
print(lista_menos100)
print(lista_mas100)
print(len(lista_mas100))
