class Animal:
    def __init__(self, animal, age):
        self.animal = animal
        self.age = age
    def info (self):
     print("L'âge de", self.animal , self.age, " ans")
    def vieillir(self):
        self.age = self.age+1
    def nommer(self):
       self.animal = input(self.animal)
       print ("L'animal se nomme", self.animal)
p1 = Animal("l'animal", 0)
p1.info()
p1.vieillir()
p1.info()
p1.nommer()
    
    