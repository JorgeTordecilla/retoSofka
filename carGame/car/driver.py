class driver():
    def isDriver(self, player):
        """asignacion de los conductores"""
        driver =[player[i] for i in range(len(player))  if player[i][2]=="si"]
        return driver