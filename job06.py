class Vehicule:
    global marque
    global annee
    global prix
    def __init__(self, marque, modele,annee, prix):
        self.marque = marque
        
        self.modele = modele

        self.annee = annee
       
        self.prix = prix
        
    def informationsVehicule(self):
        print(self.marque, self.annee, self.prix)
    def demarrer(self):
        print("Attention, je roule")
  

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes):
        Vehicule.__init__(self, marque,modele, annee, prix)
        self.portes = portes
        portes = 4
    def informationsVehicule(self):
        print("Marque =", self.marque, "\nModèle =" ,self.modele,"\nAnnée =", self.annee, "\nPrix =",self.prix,"\nNombre de porte =",self.portes)
    def demarrer(self):
        print("J'ai une plus belle voiture !")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues):
       Vehicule.__init__(self, marque, modele, annee, prix)
       self.roues = roues
       roues = 2
    def informationsVehicule(self):
        print("Marque =", self.marque,"\nModèle =", self.modele,"\nAnnée =", self.annee, "\nPrix =",self.prix,"\nNombre de roues =",self.roues)
    def demarrer(self):
        print("Je vais plus vite que vous !")
           
my_vehicle = Vehicule("Renault", "Twingo", 2000, 2000)
my_vehicle.demarrer()
my_car = Voiture("Mercedes", "Classe A", 2020, 18500, 4)
my_car.informationsVehicule()
my_car.demarrer()
my_motorbike = Moto("Yahama", "1200 Vmax", 1987, 4500, 2)
my_motorbike.informationsVehicule()
my_motorbike.demarrer()