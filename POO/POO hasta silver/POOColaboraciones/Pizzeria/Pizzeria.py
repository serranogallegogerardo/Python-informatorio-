"""
Una PIZZERÍA de la ciudad ofrece a sus clientes una amplia variedad de pizzas de fabricación propia, de varios 
- tamaños (8, 10 y 12 porciones). 

Los clientes tienen a disposición un menú que describe para 
cada una de las variedades, 
-el nombre, 
-los ingredientes y 
-el precio según 
-el tamaño y el 
-tipo (a la piedra, a la parrilla, de molde) de la pizza.

Los clientes realizan sus pedidos en el mostrador. 

El pedido debe contener el nombre del Cliente, para llamarlo cuando su pedido está listo; la cantidad de pizzas, el tamaño, la variedad, la fecha del pedido, la hora en la que el pedido debe entregarse y la demora estimada informada al cliente. 

El pedido va a la cocina y cuando está preparado se informa al que lo tomó para que se genere la factura correspondiente y se le entregue el pedido al cliente. 

El dueño de la pizzería ha manifestado la necesidad de acceder al menos a la siguiente información: 

Variedades y tipos de pizzas más pedidas por los clientes. 

Ingresos (recaudaciones) por períodos de tiempo. 

Pedidos (cantidad y monto) por períodos de tiempo. 

"""

import datetime

#def calcularHoraEntrega(hora_actual, minuto_actual, agregar_minutos_entrega, agregar_minutos_estimada):
  
def hora(fecha):
  return f'{fecha.strftime("%H")}:{fecha.strftime("%M")} hs'

def fecha(fecha):
  return f'{fecha.strftime("%d")}/{fecha.strftime("%m")}/{fecha.strftime("%Y")}'

def fechaActual():
  return datetime.datetime.now()

def calcularEntrega(min):
  return hora(datetime.datetime.now() + datetime.timedelta(minutes=min))

def calcularPrecioPedido(pedido):
  precio = 0
  for pizza in pedido.pizzas:
    precio += pizza.precio
  return precio
      
              
class Pizza:
  def __init__(self, nombre = '', ingredientes = [], tamaño_porciones = 0, precio = 0, tipo = ''):
    self.nombre = nombre
    self.ingredientes = ingredientes
    self.tamaño_porciones = tamaño_porciones
    self.precio = precio
    self.tipo = tipo

  def mostrar(self):
    print("",self.nombre, "\n", self.ingredientes, "\n", self.tamaño_porciones, "\n", self.precio, "\n", self.tipo,)

  
class Pedido:
  def __init__(self, nombre_cliente, pizzas = [], fecha_de_pedido = '', hora_entrega = '', demora_estimada = ''):
    self.nombre_cliente = nombre_cliente
    self.pizzas = pizzas
    self.fecha_de_pedido = fecha_de_pedido
    self.hora_entrega = hora_entrega
    self.demora_estimada = demora_estimada


class Pizzeria:
  def __init__(self):
    self.pedidos = []
    self.recaudaciones = 0
    self.pizzas_mas_pedidas = {}
    self.tipos_mas_pedidos = {}

  def agregarPedido(self, pedido):
    self.pedidos.append(pedido)
    self.recaudaciones += calcularPrecioPedido(pedido)
    for pizza in pedido.pizzas:
        if pizza.nombre in self.pizzas_mas_pedidas:
            self.pizzas_mas_pedidas[pizza.nombre] += 1
        else:
            self.pizzas_mas_pedidas[pizza.nombre] = 1
        if pizza.tipo in self.tipos_mas_pedidos:
            self.tipos_mas_pedidos[pizza.tipo] += 1
        else:
            self.tipos_mas_pedidos[pizza.tipo] = 1

  def recaudacionPorPeriodo(self, fecha_inicio, fecha_fin):
    monto = 0
    for pedido in self.pedidos:
      if pedido.fecha_de_pedido > fecha_inicio and pedido.fecha_de_pedido < fecha_fin:
        monto += calcularPrecioPedido(pedido)
    print('************************************')
    print(f'Fecha Desde: {fecha(fecha_inicio)}')
    print(f'Fecha Hasta: {fecha(fecha_fin)}')
    print(f'Monto de ingresos: 💲{monto}')
    print('************************************')
  
  def pedidosPorPeriodo(self, fecha_inicio, fecha_fin):
    lista = []
    monto = 0
    for pedido in self.pedidos:
      if pedido.fecha_de_pedido > fecha_inicio and pedido.fecha_de_pedido < fecha_fin:
        lista.append(pedido)
        monto += calcularPrecioPedido(pedido)
    print(f'Pedidos: {len(lista)} | Monto: {monto}')
    
    
pizzeria = Pizzeria()


anchoas = Pizza("Anchoas", ["Tomate", "Queso", "Anchoas"], 8, 1200, "Al molde")
cuatro_quesos = Pizza("4Quesos", ["Tomate", "Queso", "4 quesos"], 12, 1400, "A la parrilla")
jamonymorron = Pizza("jamonymorron", ["Tomate", "Queso", "jamon", "morron"], 10, 1600, "Al molde")


pedido1 = Pedido("Pedro", [anchoas, anchoas, cuatro_quesos, jamonymorron], datetime.datetime(2022, 7, 1, 18, 30), calcularEntrega(30), 30)

pedido2 = Pedido("Carolina", [jamonymorron, cuatro_quesos, cuatro_quesos], fechaActual(), calcularEntrega(30), 30)



pizzeria.agregarPedido(pedido1)
pizzeria.agregarPedido(pedido1)
pizzeria.agregarPedido(pedido2)

print(pizzeria.recaudaciones)

for k, v in pizzeria.pizzas_mas_pedidas.items():
  print(f'{k}: {v}')

for k, v in pizzeria.tipos_mas_pedidos.items():
  print(f'{k}: {v}')

inicio = datetime.datetime(2022,7,1)
print(inicio)
fin = datetime.datetime(2022,7,30)
print(fin)

pizzeria.recaudacionPorPeriodo(inicio, fin)

pizzeria.pedidosPorPeriodo(inicio, fin)