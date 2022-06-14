"""

clientes = [
    ["Cristian", "Gomez", 54, 123456789, ["Calle falsa 123", "Calle falsa 124", "Calle falsa 125"]],
    ["Juan", "Gonzalez", 34, 153476884, ["Calle falsa 123", "Calle falsa 124", "Calle falsa 125"]],
    ["Pedro", "De la Cruz", 33, 125456789, ["Calle falsa 123", "Calle falsa 124", "Calle falsa 125"]],
    ["Jose", "Delgado", 38, 123425789, ["Calle falsa 123", "Calle falsa 124", "Calle falsa 125"]],
    ["Maria", "Chamorro", 28, 123425789, ["Calle falsa 123", "Calle falsa 124", "Calle falsa 125"]],
    ["Juana", "Perez", 22, 123425789, ["Calle falsa 123", "Calle falsa 124", "Calle falsa 125"]],
]

for nombre, apellido, edad, numero, dict in clientes:
    print(f"| Nombre: {nombre} | Apellido: {apellido} | Edad: {edad} | Número: {numero} | Direcciones: {', '.join(dict)} |")

for i in range(len(clientes)):
    if "Cristian" in clientes[i]:
        print(f"El cliente está en la lista 'clientes[{i}]'")

 for i in cola:
      if i[0] == 'hamburguesa':
        ac_h += i[1]
      elif i[0] == 'pizza':
        ac_p += i[1]
      elif i[0] == 'empanadas':
        ac_e += i[1]

"""