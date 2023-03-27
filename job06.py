class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_width(self, width):
        self.__width = width
    def set_height(self, height):
        self.__height = height
        

    def get_width(self):
       return self.__width
    def get_height(self):
        return self.__height

my_rectangle = Rectangle(5, 10)
print (my_rectangle.get_width())
print (my_rectangle.get_height())
my_rectangle.set_width(3)
my_rectangle.set_height(4)
print (my_rectangle.get_width())
print (my_rectangle.get_height())

