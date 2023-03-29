class Personne:
    def __init__(self, age):
        self.age = age
        age = 14
    def afficherAge(self, age):
        print(self.age)
    def bonjour(self):
        print("Hello")
    def set_age(self, age):
        self.age =  age
    def get_age(self, age):
        self.age = age
    def modifier_age(self):
        my_student.get_age()
          
        
class Eleve(Personne):
    
    def allerEnCours(self):
        print ("Je vais en cours")

    def affichageAge(self):
        print ("J'ai", self.age,"ans")
    
class Professeur(Personne):
    def __init(self, matiereEnseignée):
         self.__matiereEnseignée = matiereEnseignée
    
    def enseigner(self):
        print("Le cours va commencer")

my_people = Personne(14)
my_student = Eleve(14)
my_student.affichageAge()
my_student.bonjour()
my_student.allerEnCours()
my_student.set_age(15)
my_student.affichageAge()
my_teacher = Professeur(40)
my_teacher.enseigner()