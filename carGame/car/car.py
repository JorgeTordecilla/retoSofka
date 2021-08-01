from random import randint

class car():
    def __init__(self,driverId, color, driverName):
        """creacion de carros"""
        self.driverId = driverId
        self.color = color
        self.driverName = driverName
        self.cars = list()
    def fixDriver(self,gcars):
        """lsita de objetos car"""
        self.cars.append(gcars)
    def startPosition(self,Track):
        """asignacionde carril y posicion inical"""
        for i in range(len(Track)):
            Track[i][randint(1,5)]= self.cars[0][i].driverName
        return Track