from car.track import track
from car.driver import driver
from game.game import game
from game.player import player
from car.car import car
from podium.podium import *
from random import random, randint

### creacion de objetos
Game = game(random())
drivers  =  driver()
players = game.setUpGame(int(input("Número de Jugadores: ")))
gamePodium = podium()
Track = track(randint(10,30))
##variables
inGamePlayer =  []
inGameCars =[]

##crea la lista de jugadores
for i in range(len(players)):
    inGamePlayer.append(player(players[i][0],i,players[i][1]))

## regresa cuantos jugadores son conductores
inGameDrivers = drivers.isDriver(players)
##exporta en formato json los conductores
gamePodium.jsonImport(inGameDrivers)

#crea y asigna los carros
for i in range(len(inGameDrivers)):
    cars =car(i,inGameDrivers[i][1],inGameDrivers[i][0])
    inGameCars.append(cars)
    cars.fixDriver(inGameCars)


###genera la pista aleatoria
##teniendo en cuenta que cada espacio del array es de 100mts entonces 10 =1km 30= 3km
gameTrack=Track.generateTrack(len(inGameDrivers))
##asigna la posicion de incio
gtrack = cars.startPosition(gameTrack)
##realiza la rutina de juego y devuelve los 3 primero jugadores
winners = game.gameRutine(gtrack,inGameDrivers)
##imprime el podio
gamePodium.printPodium(winners)
#####verifica el json y actualiza los valores de los ganadores
try:
    gamePodium.jsonUpdate(winners)
except:
    gamePodium.jsonImport(inGameDrivers)