# 9) Realizar una clase que administre
#una agenda.
# cada contacto almacena: nombre, teléfono y email.
# MENU:
# 1. Añadir contacto
# 2. Listar contactos
# 3. Buscar contacto
# 4. Editar contacto
# 5. Cerrar agenda

import os
import time

def menu():
    print('Agenda')
    print(' 1. Añadir contacto ')
    print(' 2. Listar contactos ')
    print(' 3. Buscar contacto ')
    print(' 4. Editar contacto ')
    print(' 5. Cerrar agenda ')


class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f'Nombre: {self.nombre} | Teléfono: {self.telefono} | E-mail: {self.email}'

class Agenda:
    def __init__(self):
        self.lista = []

    def __str__(self):
        return 'Soy una agenda xD'

    def agregar_contacto(self, nombre, numero, email, edito = False):
        contacto = Contacto(nombre, numero, email)
        self.lista.append(contacto)
        if edito == False:
          print(f'Se agregó a {self.lista[-1]}')
        else:
          print(f'Se editó a {self.lista[-1]}')
          
    def listar_contactos(self):
        index_count = 0
        for i in self.lista:
            print(f'{index_count} = {i}')
            index_count += 1

    def buscar_contacto(self, email):
        for i in range(0, len(self.lista)):
            if email == self.lista[i].email:
              print(f'Se encontró a {self.lista[i]}')
              break
        else:
          print('� No se encontró el email')
          
    def editar_contacto(self, email):
      for i in range(0, len(self.lista)):
            if email == self.lista[i].email:
              print(f'Se encontró a {self.lista[i]}')

              print('Ingrese los nuevos datos del contacto: ')
              nombre = str(input('Nombre: '))
              numero = str(input('Número: '))
              email = str(input('Email: '))
              
              self.lista.pop(i)
              
              agenda.agregar_contacto(nombre, numero, email, True)
              
              break
      else:
        print('No se encontró el email')
      


agenda = Agenda()

while True:
    os.system('clear')
    menu()

    opcion = str(input('Elegir: '))

    if opcion == '1':
        nombre = str(input('Nombre: '))
        numero = str(input('Número: '))
        email = str(input('email: '))
        agenda.agregar_contacto(nombre, numero, email)
    elif opcion == '2':
        agenda.listar_contactos()

    elif opcion == '3':
        email = str(input('Buscar por e-mail: '))
        agenda.buscar_contacto(email)

    elif opcion == '4':
        email = str(input('Editar por e-mail: '))
        agenda.editar_contacto(email)

    if opcion == '5':
        print('Gracias por usar la agenda!')
        break

    time.sleep(4)
    os.system('clear')