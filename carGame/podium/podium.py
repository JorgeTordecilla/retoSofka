import json
class podium():
    def __init__(self):
        """"valores iniciales"""
        self.scores ={}
        self.primero = 0
        self.segundo = 0
        self.tercero = 0
    def jsonImport(self, driver):
        """apertura o creacion del json"""
        try:
            with open("scores.json", "r") as file:
                data = json.load(file)
        except:
            for i in range(len(driver)):
                self.scores.update({
                    str(driver[i][0]):{
                    'veces primero':self.primero,
                    'veces segundo': self.segundo,
                    'veces tercero': self.tercero}})
                with open('scores.json', 'w') as file:
                    json.dump(self.scores, file, indent=4)

    def jsonUpdate(self, winner):
        """uppdate del json"""
        with open("scores.json", "r") as file:
            data = json.load(file)
        for i in range(3):
            if i == 0:
                value = data[winner[i]].get("veces primero")
                data[winner[i]].update({"veces primero":value+1})
            elif i == 1:
                value = data[winner[i]].get("veces segundo")
                data[winner[i]].update({"veces segundo":value+1})
            elif i == 2:
                value = data[winner[i]].get("veces tercero")
                data[winner[i]].update({"veces tercero":value+1})
            with open('scores.json', 'w') as file:
                json.dump(data, file, indent=4)

    def printPodium(self,winners):
        print("Podio: ")
        for i  in range(3):
            print(i+1,winners[i])