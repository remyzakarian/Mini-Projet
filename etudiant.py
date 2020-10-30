

class Etudiant:
    def __init__(self,num,prenom,nom,niveau):
        self.num = num
        self.prenom = prenom
        self.nom = nom
        if niveau == "A" or niveau =="B" or niveau =="C":
            self.niveau = niveau
        else:
            raise Exception("Les valeurs admises sont seulement A B ou C")

        





