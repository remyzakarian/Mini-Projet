import bd
import etudiant
import cours
import note

def printlisteetudiant(liste):
    for x in liste:
        print(x.num,x.prenom,x.nom,x.niveau,sep=", ")

def printlistecours(liste):
    for x in liste:
        print(x.num,x.intitule,x.niveau,sep=", ")

def printlistenotes(liste):
    for x in liste:
        print(x)



def main():
    bd1 = bd.BD()
    #ajouter etudiants
    print("Ajouter etudiants")
    etudiant1 = etudiant.Etudiant(1,"Remy","Zakarian","C")
    etudiant2 = etudiant.Etudiant(2,"Cyril","Zakarian","A")
    etudiant3 = etudiant.Etudiant(3,"Roula","Zakarian","B")
    etudiant4 = etudiant.Etudiant(4,"Georges" , "Zakarian", "B")
    etudiant5 = etudiant.Etudiant(5,"Edmond" , "Zakarian", "C")
    etudiant6 = etudiant.Etudiant(6,"Emilie" , "Zakarian", "A")
    etudiant7 = etudiant.Etudiant(7,"Rony" , "Zakarian", "B")
    etudiant8 = etudiant.Etudiant(8,"Bruno" , "Zakarian", "C")


    bd1.ajouteretudiant(etudiant1)
    bd1.ajouteretudiant(etudiant2)
    bd1.ajouteretudiant(etudiant3)
    bd1.ajouteretudiant(etudiant4)
    bd1.ajouteretudiant(etudiant5)
    bd1.ajouteretudiant(etudiant6)
    bd1.ajouteretudiant(etudiant7)
    bd1.ajouteretudiant(etudiant8)




    printlisteetudiant(bd1.getetudiants())
    print("##############")
    
    
    
    
    
    #supprimer etudiant 1
    print("Supprimer etudiant")
    bd1.supprimeretudiant(8)
    printlisteetudiant(bd1.getetudiants())
    
    
    print("##############")
    
    
    
    print("Editer etudiant")
    bd1.editeretudiant(3,"Roro","","")
    printlisteetudiant(bd1.getetudiants())
    print("##############")
    # # test edit etudiant
    
    
    
    print("Ajouter Cours")
    cours1 = cours.Cours(1,"Base de donnees","A")
    cours2 = cours.Cours(2,"Java 1","A")
    cours3 = cours.Cours(3,"Architecture des Machines","A")
    cours4 = cours.Cours(4,"Architecture des Systemes Informatiques","C")
    cours5 = cours.Cours(5,"Gestion de projet","B")
    
    
    
    bd1.ajoutercours(cours1)
    bd1.ajoutercours(cours2)
    bd1.ajoutercours(cours3)
    bd1.ajoutercours(cours4)
    bd1.ajoutercours(cours5)
    
    printlistecours(bd1.getcours())
    print("##############")
    
    
    
    print("Supprimer Cours")
    bd1.supprimercours(1)
    # #suppression du premier cours
    printlistecours(bd1.getcours())
    print("##############")
    
    
    
    print("Editer Cours")
    bd1.editercours(2,"Base de l'analyse Mathematique","")
    printlistecours(bd1.getcours())
    print("##############")
    
    
    
    
    
    print("Creation Note")
    note1=note.Note(2,2,12)
    note2=note.Note(3,2,8)
    note3=note.Note(4,2,15)
    note4=note.Note(3,3,10)
    note5=note.Note(2,4,12)
    
    bd1.ajouternote(note1)
    bd1.ajouternote(note2)
    bd1.ajouternote(note3)
    bd1.ajouternote(note4)
    bd1.ajouternote(note5)
    printlistenotes(bd1.getnotes())
    
    
    
    
    
    
    print("##############")
    print("Supprimer etudiant donc supprimer note")
    
    bd1.supprimeretudiant(2)
    print("Premierement suppression d'etudiant")
    printlisteetudiant(bd1.getetudiants())
    print("Deuxiemement suppression de sa note")
    printlistenotes(bd1.getnotes())
    print("##############")
    # #test si num etudiant ou num cours deja existen
    etudiant9 = etudiant.Etudiant(4,"Georges","Zakarian","B")
    cours9 = cours.Cours(3,"Web1","B")
    #bd1.ajouteretudiant(etudiant4)
    #bd1.ajoutercours(cours3)
    print("Moyenne de la classe Base de l'analyse Mathematique: ", bd1.moyenneclasse(2))
    print("##############")
    print("Moyenne de l'etudiant 3 est: ", bd1.moyenneetudiant(3))
    print("##############")
    print("Consulter notes de la classe Base de l'analyse")
    printlistenotes(bd1.consulternotesclasse(2))

    print("##############")
    print("Consulter notes de l'etudiant 3")
    printlistenotes(bd1.consulternotesetudiant(3))
    

    

main()