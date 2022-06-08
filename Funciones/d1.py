
"""
degradacion:
150 años  bolsa de plástico común 
botella de PET 1.000 años
tetrabik 30 anios
chicle 5 años 

Se solicita una función para que dado el ingreso de un elemento,

se solicite 
tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, 

e imprima la cantidad de años que tarda en degradarse.

"""

def desaf1(tipo): #declaracion formal
  if tipo == 1: 
    anio = 150 # variable local
  elif tipo == 2:
    anio = 1000
  elif tipo == 3:
    anio = 30
  elif tipo == 4:
    anio = 5
  else:
    anio = "Ingrese un numero correcto."
  return anio

tipo = int(input('Ingrese un numero:\n 1.Bolsa de plastico\n 2.Botella pet\n 3.Envase Tetrabrik\n 4.Chicle \nOpcion: '))

print(desaf1(tipo)) #declaracion actual
