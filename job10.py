class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche, reservoir):
        self.marque = marque
        self.modèle = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = en_marche
        self.__reservoir = reservoir

    def set_marque(self, marque):
        self.marque = marque
    def get_marque(self, marque):
        self.marque = marque

    def set_modele(self, modele):
        self.modele = modele
    def get_modele(self, modele):
        self.modele = modele

    def set_annee(self, annee):
        self.anne = annee
    def get_annee(self, annee):
        self.annee = annee

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage
    def get_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche
    def get_en_marche(self, en_marche):
        self.en_marche = en_marche

    def set_reservoir(self, reservoir):
        self.reservoir = reservoir
    def get_reservoir(self, reservoir):
        self.reservoir = reservoir

    def demarrer(self):
        self.en_marche = True

    def arreter(self):
        self.en_marche = False

    def reservoir(self):
        self.__reservoir = 50

    def verifier_plein(self):
        
        if self.__reservoir > 5:
         self.en_marche = True
         print ("La voiture peut démarrer")
        else:
          self.en_marche = False
          print ("La voiture ne peut pas démarrer, il n'y a pas assez de carburant")

my_car= Voiture("Citroen", "C4", 2004, 212000, "en_marche", 10)

my_car.verifier_plein()