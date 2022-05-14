#Desafio 3
#Para el uso de fertilizantes es necesario
#medir cuanto abarca un determinado compuesto 
#en el suelo el cual debe existir en una cantidad de al menos 10%
#por hectarea, y no debe existir vegetacion del tipo matorral. 
#Escribir un programa que determine si es factible la utilizacion de fertilizantes

    #ya me ingresa el porcentaje
    #el usuario ya sabe bien las cosas

vegetacion = int(input('Cuanta vegetacion existe? %'))
tipo = bool(input('Es del tipo matorral?, Enter: No - Cualquier Tecla Diferente:Si \n'))

if(vegetacion >= 10 and tipo == False):
    print('La utilizacion de fertilizantes es factible')
else:
    print('La utilizacion de fertilizantes no es factible')

