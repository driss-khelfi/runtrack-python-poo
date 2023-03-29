from math import*
class Forme:
    def __init__(self):
        print("ok")   

    def aire(self):
        a = 0
        print("L'aire de la forme est de", a, "unités carré")
class Rectangle(Forme):

    def __init__(self, width, height):
        Forme.__init__(self)
        self.width = width
        self.height = height

    def aire(self):
        a = self.width*self.height
        print("L'aire de la forme est de", a, "unités carré")
class Cercle(Forme):
    
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius
    def aire(self):
        import math
        a = self.radius*self.radius*math.pi
        print("L'aire de la forme est de", a, "unités carré")

my_form = Forme
my_form.aire(42)
my_rectangle = Rectangle(6,7)
my_rectangle.aire()
my_circle = Cercle(5)
my_circle.aire()
        
