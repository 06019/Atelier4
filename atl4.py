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

