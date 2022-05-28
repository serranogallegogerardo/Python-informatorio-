#Pido
#importe
#cantidad de tapitas

#consecuencia: codigo de descuento sobre el total(importe)
#monto total desde el inicio a final de jornada laboral

#rojo es 40, amarillo 25, blanco 0.

from turtle import color
import os

print("### CODIGOS DE DESC. P/ TAPITAS :D ###")
Estado_Tienda = True

#inicializar acumulador
total = 0

while Estado_Tienda == True:

    #recoleccion de datos
    importe = float(input('Ingrese el importe: '))
    cant_tapitas = int(input('Cantidad de tapitas: '))
    color_codigo = str(input('Ingrese el color del codigo: '))

    #Duda: Como se que color asignarle?, o eso debo 
    #usar if,elif,elif segun criterios que se me otorguen en el correspondiente ?
    total += importe

    #tratar las condiciones para descuento
    if color_codigo == 'rojo':
        descuento = 0.40
    elif(color_codigo == 'amarillo'):
        descuento = 0.25
    elif(color_codigo == 'blanco'):
        descuento = 1 # osea nada por que lo multiplicare por si mismo

    #imprimir en pantalla
    if descuento < 1:
        print('El total con descuento es:', float((importe-(importe*descuento))))
    else:
        print('El total sin descuento es:', float(importe))
    Estado_Tienda = bool(input('La tienda sigue abierta? \n Cualquier tecla -> SI \n Enter -> NO '))
    os.system('cls')
    

print('Ganancias de hoy: $', total)