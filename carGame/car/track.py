class track():
    def __init__(self,randTrack) :
        """Creacion de la ista de juego"""
        self.randTrack= randTrack
    def generateTrack(self, lendriver):
        return [[0 for _ in range(self.randTrack)] for _ in range(lendriver)]