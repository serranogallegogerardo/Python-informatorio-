# Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda.
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista1.clear()
lista1.extend(lista2)
print(lista1)