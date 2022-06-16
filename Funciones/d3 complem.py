# Un minorista en línea proporciona una 

#forma de envío urgente de 
# $10.95 para el primer elemento y 
# $2.95 para cada elemento posterior. 

# Escriba una función que 
# tome el número de elementos en el pedido
# como su único parámetro. 

# Devuelva los gastos de envío del pedido
# como resultado de la función. 

# Incluya un programa principal que
# lea la cantidad de artículos comprados al usuario y
# muestre los gastos de envío.

"""
% 2 == 0 par
0 2 4 6 8
% 2 != 0 impar
1 3 5 7
"""

def pedido(nro_elementos): # 32
  gastos_envio_pedido = 10.95
  if nro_elementos > 1: # 4
    for i in range(nro_elementos-1):
      gastos_envio_pedido += 2.95
  return gastos_envio_pedido

# 3 = 10.95 + 2.95 + 2.95
#main
cant_articulos_comprados = int(input('Ingrese la cantidad de artículos: ')) 

print(f'Los gastos del envio por {cant_articulos_comprados} artículos.')
print(f'Total: {pedido(cant_articulos_comprados):.2f} $')
