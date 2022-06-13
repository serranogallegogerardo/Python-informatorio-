"""
Leer una frase y luego invierta el orden de las palabras en la frase. Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en “palabras mil por vale imagen una”.
"""

frase = "una imagen vale por mil palabras"
palabraActual = ""
fraseMod = ""
"""
for i in reversed(frase):
  if i == " ":
    fraseMod += palabraActual[::-1] + " "
    palabraActual = ""
  else:
    palabraActual += i
fraseMod += palabraActual[::-1] + " "

print(fraseMod)

#print(cad[0:])
#print(cad[::-1])
"""

for i in frase:
  if i == " ":
    fraseMod = palabraActual + " " + fraseMod
    palabraActual = ""
  else:
    palabraActual += i
    
fraseMod = palabraActual + " " + fraseMod

print(fraseMod)
