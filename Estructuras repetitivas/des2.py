print('### CAMPAÑA DE CIGARRILLOS ###')
op = True

#Acumuladores a 0

Total_100 = 0
Total_100a200 = 0
Total_200 = 0

#Definicion para evitar errores
personas_100 = 0
personas_100a200 = 0
personas_200 = 0

while op == True:
    #Recoleccion de datos
    cant_colillas = float(input(' ---- Ingrese la cantidad de colillas de cigarrillos ---- '))
    cant_personas = int(input(' ---- Ingrese la cantidad de personas que recolectaron esas colillas ---- '))

    #Acumuladores p/ porcentajes
    if cant_colillas < 100:
        personas_100 = cant_personas
        #Me parece que esta de mas
        Total_100 =+ cant_colillas
    elif(cant_colillas >= 100 and cant_colillas < 200):
        personas_100a200 = cant_personas
        #Me parece que esta de mas
        Total_100a200 =+ cant_colillas
    elif(cant_colillas > 199):
        personas_200 = cant_personas
        #Me parece que esta de mas
        Total_200 =+ cant_colillas 

    #itero nuevamente?
    op = bool(input('Desea agregar mas datos? \n 1.Cualquier tecla -> SI \2. Enter -> NO'))

#Mostrar el output porcentajes
#total de colillas
Total_General_Colillas = Total_100 + Total_100a200 + Total_200
#total de personas

Total_General_Personas = personas_100 + personas_100a200 + personas_200
print('Porcentaje de personas que han encontrado menos de 100')
print((personas_100//int(Total_General_Personas)) * 100 )
print('Porcentaje de personas que han encontrado mas de 100 y menos de 200')
print((personas_100a200//int(Total_General_Personas)) * 100 )
print('Porcentaje de personas que han encontrado mas de 200')
print((personas_200//int(Total_General_Personas)) * 100 )

