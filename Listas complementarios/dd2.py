"""
Desafío 2

Crea una tupla con los factores que más afectan a los mares. 
Luego para jugar con niños y niñas, ??????????

aprendiendo sobre contaminación del agua 

crea un programa que pida números,
si el numero esta entre 1
y la longitud máxima de la tupla,

 muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero.
"""

factores = ("Las aguas residuales","Las sustancias químicas tóxicas","Las aguas pluviales")
#genero = ("niño","niña")

print('### PROGRAMA ECOLOGICO ###')
print("factores que afectan al mar")

for i in range(1,3,1):
    print(factores[i])

op = '1'

while op == '1':
    print(('ingrese un numero entre 0 y ', len(factores)-1))
    n = int(input())

    if n <= len(factores):
        print(factores[n])
    else:
        print('error')
    
    print('Desea utilizar nuevamente el programa?')
    op = input('1: Si, Otro: No')
