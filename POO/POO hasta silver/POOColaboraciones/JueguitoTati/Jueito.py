#Tenis - Sayayin
"""En un partido de tenis, un jugador empieza con una puntuación de 0. Con cada pelota exitosa, el jugador gana más puntos de la 
siguiente manera: 0 → 15 → 30 → 40 

Si un jugador llega a los 40 puntos y vuelve a obtener una pelota exitosa, ganará un game. 
(En la medida que el otro jugador no tenga 40 puntos también). 

Si ambos jugadores alcanzan 40 puntos que se conoce como deuce. 

Deuce>> Una pelota exitosa obtenida en estado de deuce, otorga una ventaja al jugador. 
Si el jugador contrario marcará nuevamente el marcador vuelve a deuce. Si un jugador se encuentra en ventaja y marca otra vez, 
ese jugador gana el game. 

Tie Brake>> La partida gana cuando un jugador gana 3 sets. Cada set se gana si un jugador llega a 6 games, 
siempre y cuando tenga diferencia de 2 games con su contrincante. En caso de que ambos lleguen a 6 games ese set se 
definirá por Tie brake. Aquí la secuencia de puntos es de 1 en 1 y gana el primero que llega a 7 puntos con diferencia de 2. 
En caso de llegar a 6-6 el ganador deberá estirarse hasta 8-6 y así sucesivamente.

Escriba un programa para manejar cada uno de estos requisitos de puntuación: 
Los jugadores deben ser capaces de sumar puntos.

El juego debe ser capaz de terminar con un ganador.

El caso de "deuce" debe ser manejado.

El caso de “Tie Brake” debe ser manejado también.

Después de que un juego haya sido ganado, se debe poder determinar al ganador.

Se debe poder obtener la puntuación actual de cualquier jugador en cualquier momento durante el juego. """


from random import random
import random
import time

class Game:
    def __init__(self, jugador1,jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.puntos = [0,15,30,40]
        self.posicion1 = 0
        self.posicion2 = 0
        self.ganador = ''
       
    def Deuce (self):
        if self.posicion1 == 3 and self.posicion2 == 3:
            return True
    def FinDeuce(self):
        if (self.posicion1 > self.posicion2 and self.posicion1 == len(self.puntos)+2) or (self.posicion2 > self.posicion1 and self.posicion2 == len(self.puntos)+2) :
            return  True      

    def JuegoGame (self):
        jugadores = [self.jugador1,self.jugador2]               
        while not self.Deuce() :
            #time.sleep(2)
            ganadorpunto = random.choice(jugadores)
            print(f' punto para {ganadorpunto}')
            if self.posicion1 == 3 or self.posicion2 == 3:
                #time.sleep(1)
                print(f'GANADOR DEL GAME : {ganadorpunto}')
                self.ganador = str(ganadorpunto)
                break
            if ganadorpunto == self.jugador1:
                #time.sleep(1)
                self.posicion1 +=1
                print(f'{self.puntos[self.posicion1]}/{self.puntos[self.posicion2]}')
            elif ganadorpunto == self.jugador2:
                #time.sleep(1)
                self.posicion2 +=1
                print(f'{self.puntos[self.posicion1]}/{self.puntos[self.posicion2]}')
        else:          
            pj1=0
            pj2=0 
          
            while pj1 !=2 and pj2 != 2:
                ganadorpunto = random.choice(jugadores)
                print(f' punto para {ganadorpunto}')
                if ganadorpunto == self.jugador1:
                    pj1 += 1                    
                elif ganadorpunto == self.jugador2:   
                    pj2 += 1                        
                if pj1 > pj2 and pj1 != 2:
                  print('--------------------------------')
                  print(f'Ventaja para {self.jugador1}')
                  print('--------------------------------')
                elif pj2 > pj1 and pj2 != 2:
                  print('--------------------------------')
                  print(f'Ventaja para {self.jugador2}') 
                  print('--------------------------------')
                if pj1 == 1 and pj2 == 1:
                  pj1 =0
                  pj2 =0
                  print('--------------------------------')
                  print('¡DEUCE!')
                  print('--------------------------------')
                elif pj1 == 2:
                  print(f'GANADOR DEL GAME : {self.jugador1}')
                  self.ganador = str(ganadorpunto)
                elif pj2 == 2:
                  print(f'GANADOR DEL GAME:  {self.jugador2}') 
                  self.ganador = str(ganadorpunto)

                  
    def Ganador (self):
        return self.ganador 
                   

  
          
      


primergame = Game('pedro','juan')

primergame.JuegoGame()
 