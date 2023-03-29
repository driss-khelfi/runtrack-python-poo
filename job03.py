class Rectangle:
    global width
    global height
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def perimetre(self):
        p = (self.height*2)+(self.width*2)
        print("le périmètre du rectangle est de", p, "unités")

    def surface(self):
        s = self.height*self.width
        print("la surface du rectangle est de", s, "unités carré")

    def set_width(self):
        self.width = width
    def get_width(self):
        self.width = width

    def set_heigth(self):
        self.height = height
    def get_height(self):
        self.height = height

class Parallélépipède(Rectangle):
    def __init__(self, width, height, depth):
        Rectangle.__init__(self, width, height)
        self.depth = depth
    def volume (self):
        v = self.width*self.height*self.depth
        print ("Le volume du parallélépipède rectangle est de", v, "unités cube")

my_rectangle = Rectangle(3,4)
my_parallelepipede = Parallélépipède(3,4,5)
my_rectangle.perimetre()
my_rectangle.surface()
my_parallelepipede.volume()