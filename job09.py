class Student:
    
    def __init__(self, prenom, nom, numero, credit, level):
        self.prenom = prenom
        self.nom = nom
        self.numero = numero
        self.credit = credit
        self.level = level

    def add_credits(self):
        x = 10
        self.credit=self.credit+x
        print("Le nombre de credits de", self.prenom, self.nom, "est de", self.credit, "points")
   
    def studentEval(self):
       if self.__credit >= 90:
        Student.get_level = "Excellent"
       elif self.__credit >= 80 and self.__credit<90:
        Student.get_level = "Très bien"
       elif self.__credit >= 70 and self.__credit<80:
        Student.get_level = "Bien"
       elif self.__credit >= 60 and self.__credit<70:
        Student.get_level = "Passable"
       elif self.__credit <60:
        Student.get_level = "Passable"
    
    def studentInfo(self):
     print("Nom: ",self.nom)
     print("Prenom: ", self.prenom)
     print("Numero: ", self.numero)
     print("Level: ", self.level)


      
       
Etudiant = Student("John", "Doe", 145, 0, "level")
for _ in range(9):
 Etudiant.add_credits()
Etudiant.studentInfo()



