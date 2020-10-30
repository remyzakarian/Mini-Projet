import etudiant
import cours
import note
import statistics
class BD:
    
    etudiants= list()
    cours1= list()
    notes= list()

    def __init__(self):
        pass

    def getetudiants(self):
        return self.etudiants
    
    def getcours(self):
        return self.cours1
    
    def getnotes(self):
        etudiantTrouve = False
        coursTrouve = False
        listenotesfull = []
        for x in self.notes:
            for y in self.etudiants:
                if x.numEtudiant == y.num:
                    etudiantTrouve = True
                    listenumeroetudiant = x.numEtudiant
                    listeprenometudiant = y.prenom
                    listenometudiant = y.nom
                    listeniveauetudiant = y.niveau
            
            for z in self.cours1:
                if x.numCours == z.num:
                    coursTrouve = True
                    listenumerocours = z.num
                    listeintitulecours = z.intitule
                    listeniveaucours = z.niveau
                    listenote= x.note
            if etudiantTrouve and coursTrouve:
                listenotesfull.append([listenumeroetudiant,listeprenometudiant,listenometudiant,listeniveauetudiant,listenumerocours,listeintitulecours,listeniveaucours,listenote])
        return listenotesfull

    def ajouteretudiant(self,a):
        if isinstance(a,etudiant.Etudiant):
            for x in self.etudiants:
                if x.num == a.num:
                    raise Exception("Num Deja Existe")
            self.etudiants.append(a)
        else:
            raise Exception("Type n'est pas etudiant")
    
    def supprimeretudiant(self,num):
        # supprimer etudiant de table etudiant et ses notes
        for x in self.etudiants:
            if x.num == num:
                self.etudiants.remove(x)
        for y in self.notes:
            if y.numEtudiant == num:
                self.notes.remove(y)
    
    def editeretudiant(self,num,prenom,nom,niveau):
        # si prenom ou nom ou niveau sont vides donc il ne faut pas les changer
        for x in self.etudiants:
            if x.num == num:
                if prenom== "":
                    x.prenom = x.prenom
                else:
                    x.prenom = prenom
                if nom== "":
                    x.nom = x.nom
                else:
                    x.nom = nom
                if niveau== "":
                    x.niveau = x.niveau
                else:
                    x.niveau = niveau
    
    def ajoutercours(self,a):
        if isinstance(a,cours.Cours):
            for x in self.cours1:
                if x.num == a.num:
                    raise Exception("Num Deja Existe")
            self.cours1.append(a)
        else:
            raise Exception("Type n'est pas cours")
    
    def supprimercours(self,num):
        for x in self.cours1:
            if x.num == num:
                self.cours1.remove(x)
    
    def editercours(self,num,intitule,niveau):
        # si prenom ou nom ou niveau sont vides donc il ne faut pas les changer
        for x in self.cours1:
            if x.num == num:
                if intitule== "":
                    x.intitule = x.intitule
                else:
                    x.intitule = intitule
                if niveau== "":
                    x.niveau = x.niveau
                else:
                    x.niveau = niveau

    def ajouternote(self,a):
        if isinstance(a,note.Note):
            self.notes.append(a)
        else:
            raise Exception("Type n'est pas Note")

    def supprimernote(self,numEtudiant, numCours):
        for x in self.notes:
            if x.numEtudiant == numEtudiant and x.numCours == numCours:
                self.notes.remove(x)

    def editernote(self,numEtudiant,numCours,note):
        for x in self.notes:
            if x.numEtudiant == numEtudiant and x.numCours == numCours:
                x.note = note

    def moyenneclasse(self,num):
        #je considere qu'un cours est une classe

        def filtrerclasse(x):
            if x.numCours == num:
                return True
            else:
                return False       
        #print(list(filter(lambda x: x[0].numCours == num , self.notes)))
        a = list(filter(filtrerclasse,self.notes))  
        
        #c'est une liste avec toutes les notes du cours num
        notedeliste = []
        for x in a:
            notedeliste.append(x.note)
        return statistics.mean(notedeliste)


    def moyenneetudiant(self,num):
        #je considere qu'un cours est une classe

        def filtreretudiant(x):
            if x.numEtudiant == num:
                return True
            else:
                return False       
        #print(list(filter(lambda x: x[0].numCours == num , self.notes)))
        a = list(filter(filtreretudiant,self.notes))  
        
        #c'est une liste avec toutes les notes du cours num
        notedeliste = []
        for x in a:
            notedeliste.append(x.note)
        return statistics.mean(notedeliste)

    def consulternotesclasse(self,numCours):
        def filtrerclasse(x):
            if x.numCours == numCours:
                return True
            else:
                return False       
        #print(list(filter(lambda x: x[0].numCours == num , self.notes)))
        a = list(filter(filtrerclasse,self.notes))  
        notesdescription = []
        for x in a:
            for y in self.cours1:
                if x.numCours == y.num:
                    numCours = y.num
                    nomCours = y.intitule
                    niveauCours = y.niveau
            for z in self.etudiants:
                if x.numEtudiant == z.num:
                    numEtudiant = z.num
                    prenomEtudiant = z.prenom
                    nomEtudiant = z.nom
                    niveauEtudiant = z.niveau
            note = x.note
            notesdescription.append([numCours,nomCours,niveauCours,numEtudiant,prenomEtudiant,nomEtudiant,niveauEtudiant,note])
        return notesdescription

            
    def consulternotesetudiant(self,numEtudiant):
        def filtreretudiant(x):
            if x.numEtudiant == numEtudiant:
                return True
            else:
                return False       
        #print(list(filter(lambda x: x[0].numCours == num , self.notes)))
        a = list(filter(filtreretudiant,self.notes))  
        notesdescription = []
        for x in a:
            for y in self.etudiants:
                if x.numEtudiant == y.num:
                    numEtudiant = y.num
                    prenomEtudiant = y.prenom
                    nomEtudiant = y.nom
                    niveauEtudiant = y.niveau
            for z in self.cours1:
                if x.numCours == z.num:
                    numCours = z.num
                    nomCours = z.intitule
                    niveauCours = z.niveau
            note = x.note
            notesdescription.append([numEtudiant,prenomEtudiant,nomEtudiant,niveauEtudiant,numCours,nomCours,niveauCours,note])
        return notesdescription