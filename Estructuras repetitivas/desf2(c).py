#Segunda opcion desafio 2

print('### CAMPAÑA DE CIGARRILLOS ###')
op = True

#Acumuladores a 0

Total_100 = 0
Total_100a200 = 0
Total_200 = 0

#es la cantidad de personas que recolectaron menos de 100
#entre 100 y 200
#y mas de 200

#creo que podria poner un while aca para ir pidiendole las cantidades

print(' ---- Ingrese la cantidad de personas que recolectaron esas colillas  ---- ')
Total_100 = int(input('Menos de 100: '))
Total_100a200 = int(input('100 y 199: '))
Total_200 = int(input('Mas de 200: '))

#total de personas
Total_General_Personas = Total_100 + Total_100a200 + Total_200
print('Porcentaje de personas que han encontrado menos de 100')
print(round((Total_100/Total_General_Personas) * 100) , '%')
print('Porcentaje de personas que han encontrado mas de 100 y menos de 200')
print(round((Total_100a200/Total_General_Personas) * 100) , '%')
print('Porcentaje de personas que han encontrado mas de 200')
print(round((Total_200/Total_General_Personas) * 100) , '%')

