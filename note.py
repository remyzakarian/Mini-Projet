import cours
import etudiant
import bd
class Note:
    def __init__(self,numEtudiant,numCours,note):
        
        etudiantexiste = False
        coursexiste = False
        ##verifier si etudiant est dans le DB et si le cours est dans la BD
        for x in bd.BD.etudiants:
            if x.num == numEtudiant:
                etudiantexiste = True
        for y in bd.BD.cours1:
            if y.num == numCours:
                coursexiste = True
        
        if etudiantexiste and coursexiste:
            self.numEtudiant = numEtudiant
            self.numCours = numCours
            self.note = note
        else:
            raise Exception("Etudiant ou Cours pas dans BD")
        
    


