"""
DESAFÍO 4
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6
"""
print('Ingrese el tamano de su tabla')
f = int(input('Fila: '))
c = int(input('Columna: '))
#print("🟢⚪")


for i in range(0,f,1):
  
  #if i % 2 == 0: 
  for j in range(0,c,1):

    #3x4
    #2x4
    
    if (i % 2 == 0) and (j % 2 == 0) or (i % 2 != 0) and (j % 2 != 0):
      print("🟢", end = '')
    else:
      print("⚪", end = '')

      
  print('')

      #2:2, 2:4, 2:6
      #4:2, 4:4, 4:6


      

    #[npar][npar]
    #si j es par entonces verde
    

"""
  
    1 0 1 0 1  
    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0

    a[0][0]
    a[0][2]
    a[0][4]

    a[2][0]
    a[2][2]
    a[2][4]
"""