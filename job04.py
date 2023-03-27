class SePresenter:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    def presentation(self):
     print("Je suis " + self.prenom + " " + self.nom)

p1 = SePresenter("John", "Doe")
p1.presentation()
p1 = SePresenter("Jean", "Dupont")
p1.presentation()


