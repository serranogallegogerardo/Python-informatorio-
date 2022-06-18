"""
Ejercicio 8: Capitalízalo

En este ejercicio, escribirá una 

función que capitaliza los caracteres apropiados en una cadena.
Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y seguida de un espacio. 

El primer carácter de la cadena también debe estar en mayúscula, 
así como el primer carácter no espacial después de un ".", "!" o "?"

Por ejemplo, si la función se proporciona con la cadena: 
"¿a qué hora tengo que estar allí? ¿cuál es la dirección?" 
entonces debería devolver la cadena:
"¿A qué hora tengo que estar allí? ¿Cuál es la dirección?".

Incluya un programa principal que lea una cadena del usuario, la capitalice utilizando su función y muestre el resultado.
"""

def capitalizar(cadena):
    cadena = cadena.capitalize()
  # así como el primer carácter no espacial después de un ".", "!" o "?"
    capitalizar_siguiente = False
    cadena = list(cadena)
    for i in range(len(cadena)):
        if cadena[i] == '.' or cadena[i] == '!' or cadena[i] == '?' or cadena[i] == '¿' and capitalizar_siguiente == False:
            capitalizar_siguiente = True
        elif capitalizar_siguiente == True:
          cadena[i] = cadena[i].capitalize()
          capitalizar_siguiente = False
    return "".join(cadena) # Para unir listas a string

cad2 = "¿a qué hora tengo que estar allí? ¿cuál es la dirección?"
cad = input('Ingrese su frase: ')

print(f'La frase capitalizada es: {capitalizar(cad)}')
print(f'CAD2: {capitalizar(cad2)}')