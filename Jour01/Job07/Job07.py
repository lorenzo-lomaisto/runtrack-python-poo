class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
    
    # Assesseurs pour chaque attribut
    def get_titre(self):
        return self._titre
    
    def get_auteur(self):
        return self._auteur
    
    def get_nb_pages(self):
        return self._nb_pages
    
    # Mutateurs pour chaque attribut
    def set_titre(self, titre):
        self._titre = titre
    
    def set_auteur(self, auteur):
        self._auteur = auteur
    
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self._nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")
    
    def __str__(self):
        return f"Livre : {self._titre} - Auteur : {self._auteur} - Nombre de pages : {self._nb_pages}"

livre1 = Livre("Harry Potter et la Coupe de feu", "J.K. Rowling", 636)
print(livre1.get_titre())        
print(livre1.get_auteur())       
print(livre1.get_nb_pages())   
print(livre1.get_titre())        
print(livre1.get_auteur())       
print(livre1.get_nb_pages())     
    

 

