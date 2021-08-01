from random import random, randint
class game():
    def __init__(self, gameId):
        """asigna un id aleatorio al juegpp"""
        self.gameId = gameId
    def setUpGame(numberplayer):
        """inicio del juego"""
        player=[[input("Nombre: "), input("Color carro: "), input("Es conductor?: ")] for i in range(numberplayer)]
        return player
    def gameRutine(track, driver):
        """rutina de juego"""
        winner = list()
        win = False
        while not win:
            for i in range(len(track)):
                dice = randint(1,6)
                inde= track[i].index(driver[i][0])
                if dice+inde >= len(track[i]) or  track[i][-1]  == driver[i][0]:
                    track[i][inde] = dice
                    track[i][-1]  = driver[i][0]
                    if driver[i][0] not in winner:
                        winner.append(driver[i][0])
                    continue
                track[i][inde] = dice
                track[i][inde+dice] =driver[i][0]
            if len(winner)==len(driver) or  len(winner) == 3:
                win = True
        return winner
