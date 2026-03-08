class Employee:
    def __init__(self, numPerm, nom,prenom,):
        self.numero_Permis = numPerm
        self.nom=nom
        self.prenom=prenom
        self.etat = False
        self.voiture = None
    def afficher_Info(self):
        print(f" l'employer : {self.nom} {self.prenom} a un permis avec ce numero : {self.numero_Permis}")
        if self.etat == True:
            print(f"il a pris la voiture matricule avec : {self.voiture.matricule}")

        else:
            print("il n'a pas pris une voiture !")

    def affecter_Voiture(self,voiture):
        if self.etat == True:
            print("il a deja  pris une voiture !")
        else :
            self.voiture = voiture
            self.etat = True
            print("voiture affectee a votre employe !")
            voiture.chauffeur = self
    def retirer_voiture(self,voiture):
        if self.etat == True:
            self.etat = False
            print ("voiture retiree a votre employe !")
        else :
            print("il a pas pris cette voiture pour la retirer!")


class Voiture:
    def __init__(self, matricule,annee,marque,kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.etat = False
        self.chauffeur = None
    def afficher_Info(self):
        print (f"cette voiture matriculee : {self.matricule} , anne de sortie: {self.annee} d'une marque : {self.marque} , kilometrage: {self.kilometrage}")
        if self.etat == True:
            print(f"cette  voiture est pris par ce chauffeur : {self.chauffeur.nom} {self.chauffeur.prenom} {self.chauffeur.prenom} et son numero de permis est : {self.chauffeur.numero_Permis} ")
        else:
            print(" voiture disponible !")

e1=Employee("a0011","ferhat","mehdioui")
e2=Employee("b0022","ali","manis")
e3=Employee("c0033","zizou","laala")
v1=Voiture("mob06",2004,"TOYOTA",200000)
v2=Voiture("abc50",2014,"KIA",164000)
v3=Voiture("mkjs8",2010,"TOYOTA",225000)

e1.affecter_Voiture(v1)
e2.affecter_Voiture(v2)
e3.affecter_Voiture(v3)
e1.afficher_Info()
e2.afficher_Info()
e3.afficher_Info()

