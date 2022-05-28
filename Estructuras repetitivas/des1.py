
import os

print('### Bievenido a THE BANK ###')

print('# LOGIN #')
user = input('Usuario: ') # Usuario que pido: Gera
password = input('Password: ') # Password: Gera321

for i in range(1,3,1):

    if (user == 'Gera') and (password == 'Gera321'):
        print('Ud a ingresado correctamente')
        break
    else:
        print('Ud. ingreso mal usuario o contraseña.')
        print('Ingrese nuevamente los datos:')
        user = input('Usuario: ') 
        password = input('Password: ') 

        #Ignorar esto:
        os.system('cls')
