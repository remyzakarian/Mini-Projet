class Cours:
    def __init__(self,num,intitule,niveau):
        self.num = num
        self.intitule = intitule
        if niveau == "A" or niveau =="B" or niveau =="C":
            self.niveau = niveau
        else:
            raise Exception("Les valeurs admises sont seulement A B ou C")