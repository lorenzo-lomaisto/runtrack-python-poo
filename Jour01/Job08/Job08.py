class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

    def afficher_livre(self):
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Nombre de pages : {self.__nb_pages}")
        print(f"Disponible : {self.__disponible}")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")


livre1 = Livre("Harry Potter et la Coupe de feu", "J.K. Rowling", 636)
livre1.afficher_livre()

# Emprunter le livre (il est disponible)
livre1.emprunter()

# Afficher à nouveau les attributs du livre
livre1.afficher_livre()

# Emprunter le livre à nouveau (il n'est pas disponible)
livre1.emprunter()

# Rendre le livre (il n'est plus emprunté)
livre1.rendre()

# Afficher une dernière fois les attributs du livre
livre1.afficher_livre()