"""
Escribir un programa que pregunte a diferentes personas cuánto 
conocen sobre contaminación del 1 al 10,
almacene estos valores en una lista y los muestre
 por pantalla ordenados de menor a mayor.
"""


L = []
op = 1
while (op == 1):
    
    print('cuanto conoce sobre contaminacion? ?/10 ')
    puntaje = int(input())

    L.append(puntaje)

    op = int(input('1:seguir - otro: cortar'))
    

print(sorted(L))
