from random import*

class Jeu:
    
    def __init__(self, paquet):
        self.paquet = paquet

paquet = ["as de pique", "2 de pique", "3 de pique", "4 de pique", "5 de pique", "6 de pique", "7 de pique",
          "8 de pique", "9 de pique", "10 de pique", "valet de pique", "dame de pique", "roi de pique",
          "as de coeur", "2 de coeur", "3 de coeur", "4 de coeur", "5 de coeur", "6 de coeur", "7 de coeur",
          "8 de coeur", "9 de coeur", "10 de coeur", "valet de coeur", "dame de coeur", "roi de coeur",
          "as de trèfle", "2 de trèfle", "3 de trèfle", "4 de trèfle", "5 de trèfle", "6 de trèfle", "7 de trèfle",
          "8 de trèfle", "9 de trèfle", "10 de trèfle", "valet de trèfle", "dame de trèfle", "roi de trèfle",
          "as de carreau", "2 de carreau", "3 de carreau", "4 de carreau", "5 de carreau", "6 de carreau", "7 de carreau",
          "8 de carreau", "9 de carreau", "10 de carreau", "valet de carreau", "dame de carreau", "roi de carreau"]
paquet2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
           1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
           1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
           1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
class Cartes(Jeu):

    def __init__(self, paquet, valeur, couleur):
        Jeu.__init__(self, paquet)
        self.valeur = valeur
        self.couleur = couleur

    def set_valeur(self, valeur):
        self.valeur = valeur
    def get_valeur(self, valeur):
        self.valeur = valeur

    def set_couleur(self, couleur):
        self.couleur = couleur
    def get_couleur(self, couleur):
        self.couleur = couleur

    def melanger(self):
        import random
        hasard = random.choice(paquet2)
        valeur = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi" ]
        if hasard == 1:
            input("1'(appuyez sur la touche U) ou 11 (appuyez sur la touche O)")
            if input == "o" or input=="O":
               hasard = 11
            elif input == "u" or input == "U":
                print("ok")    
            
              
        mes_cartes.append(hasard)
        paquet2.remove(hasard)
       
    
    def piocher(self):
        print(self.joueur, ", vous avez pioché un", self.valeur, "de", self.couleur )

    def ajouter(self):
        
        print(mes_cartes)
    def somme(self):
        s = mes_cartes[0]+mes_cartes[1]
        print("la somme des 2 cartes piochées est de", s)

   

mes_cartes = []
cartes_du_croupier = []
import random

ma_carte = Cartes("Joueur1", "roi", "trèfle")


for _ in range(2):
 ma_carte.melanger()
 ma_carte.set_valeur(random.choice(paquet2))
 ma_carte.ajouter()
ma_carte.somme()
