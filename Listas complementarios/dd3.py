"""
Desafío 3
Crea un diccionario donde la clave sea el nombre de biólogos 
y el valor sea el email (no es necesario
validar). 
-----------
Tendrás que ir pidiendo contactos 
hasta el usuario diga que no quiere insertar mas. 
No se podrán insertar nombres repetidos.
-----------

"""
 # remplace gmail por aporte
"""
Charles Darwin y su teoría de la evolución.
Gregor Mendel, el padre de la genética.
Galeno de Pérgamo y sus experimentos.
Hipócrates de Cos, el padre de la medicina.
Aristóteles y sus aportaciones a la biología.
"""
"""
#practica
Biologos = {
    #nombre y aporte
    'Charles Darwin':'teoría de la evolución.',
    'Gregor Mendel':'el padre de la genética.',
    'Galeno de Pérgamo':'sus experimentos.',
    'Hipócrates de Cos':'el padre de la medicina.',
    'Aristóteles':'sus aportaciones a la biología.'
}
"""

dictuser = {}

user = '1'

while user == '1':

    Nombre = input('Nombre:')
    Mail = input('Mail:')
    
    dictuser.update({Nombre:Mail})

    user = input('1: Agregar - Otro: Salir')

print(dictuser)



