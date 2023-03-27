class Livre:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def set_pages(self, pages):
        self.__pages = pages

    def get_title(self):
       return self.__title
    def get_author(self):
        return self.__author
    def get_pages(self):
     def my_int():
      while True:
        try:
         pages = int
        except ValueError:
         print("Erreur: Ce n'est pas un nombre valide")
         continue
        if pages < 0:
         print("Erreur: Votre nombre doit être positif")
         continue
        else:
         break
     return self.__pages
    
    print ("Ce n'est pas un nombre de pages valide!")

my_book = Livre("L'Etranger", "Albert Camus", 159)
print (my_book.get_title())
print (my_book.get_author())
print (my_book.get_pages())

my_book.set_title("Le Petit Prince")
my_book.set_author("Antoine de Saint Exupery")
my_book.set_pages(93)
print (my_book.get_title())
print (my_book.get_author())
print (my_book.get_pages())