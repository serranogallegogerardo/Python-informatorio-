#Tenemos que decidir entre 2 recetas ecologicas. los ingredientes para cada
#tipo de receta aparecen a continaucion

# separado para ecologico:


## ingredientes receta 1: 
# ingredientes receta 2


# lentejas y apio
## : Morron y Cebolla


## ingredientes comunes: verduras o berenjena

#Escribir un programa que pregunte al usuario que tipo de receta desea
#y en funcion de su respuesta
#  le muesstre un menu con los ingredientes disponibles para que elija.

#  solo se pued elegir 3 ingredientes(entre la receta elegida y los comunes) y el tipo de receta.

# 2Al final 
#mostrar por pantalla la receta elegida y todos los ingredientes
# ejemplo: receta1, verdura

print('Bienvenido a recetas ecologicas v3000')
print('------------------------------------------')
print('Receta con Ingredientes: ')
print('receta 1')
print('receta 2')
RecetaTipo = int(input('Ingrese su receta (numero):'))
if(1 == RecetaTipo):
    print('[Lentejas y Apio]')
    res = 'Lentejas, Apio'
else:
    print('[Morron y Cebolla]')
    res = 'Morron, Cebolla'
print('Usted selecciono: ', RecetaTipo)
print('-------------------------------------------')

print('1. Verdura')
print('2. Berenjena')
RecetaTipo = int(input('Ingrese el ingrediente adicional (numero): ')) 

if(1 == RecetaTipo):
    RecetaTipo = 'Verdura'
else:
    RecetaTipo = 'Berenjena'

print('Usted selecciono el ingrediente adicional: ', RecetaTipo)

print('El pedido tiene: ', res,' y ', RecetaTipo)