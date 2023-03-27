class Livre:
    def __init__(self, title, author, pages, available):
     self.__title = title
     self.__author = author
     self.__pages = pages
     self.__available = available

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_pages(self, pages):
        self.__pages = pages

    def set_available(self, available):
        self.__available = available

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
    
    def get_available(self):
       return self.__available
    
      
    def verification(self, available):
       if self.__available== True:
          print("Ce livre est disponible")
          return self.__availaible  
       else:
         print("Ce livre n'est pas disponible")
         print("Ce livre est disponible")

    def emprunter(self):
      my_book.set_available(False)
      return self.__available
      
      
      
      
      

    
    def rendre(self):
      my_book.set_available(False)
      return self.__available

my_book = Livre("L'Etranger", "Albert Camus", 159, True)
print (my_book.get_title())
print (my_book.get_author())
print (my_book.get_pages())
print (my_book.get_available())
my_book.emprunter

print (my_book.get_available())
my_book.rendre
print (my_book.get_available())