cant_vehiculos = 0.0
cant_vehiculos_basura = 0.0
cant_vehiculos_multa = 0.0

op = 1

while op != 0:
    numeros = str(input('5 dig:'))
    #cantidad de vehiculos
    cant_vehiculos += 1
    #cantidad de vehiculos con pos4 = 1
    if((numeros[3] == '1')):
        cant_vehiculos_basura += 1

    if((numeros[4] == '1')):
        cant_vehiculos_multa += 1

    #op = bool(input('Desea utilizar nuevamente el programa?\nCualquier letra:Continuar\nEnter:Cerrar\n'))
    op = int(input('0Salir - 1Seguir'))

print('La cantidad de vehiculos es de ', cant_vehiculos)
print('la cantidad de vehiculos que tiraron basura es de: ', cant_vehiculos_basura)
print('Porcentaje de vehiculos que ya tenian multa sobre el total: ', (float(cant_vehiculos_multa/cant_vehiculos))*100 ,'%')

#letras es patente
#3 primeros es patente 
#99900

#cantidad de vehiculos
#cantidad de vehiculso con pos4 = 1

#total de vehiculos multados 
# -> porcentaje de cuantos ya tenian multa
