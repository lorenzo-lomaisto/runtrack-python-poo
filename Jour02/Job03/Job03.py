class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


rectangle1 = Rectangle(5, 3)
print(rectangle1.perimetre()) # 16
print(rectangle1.surface()) # 15
rectangle1.set_longueur(7)
rectangle1.set_largeur(4)
print(rectangle1.perimetre()) # 22
print(rectangle1.surface()) # 28

parallelepipede1 = Parallelepipede(5, 3, 2)
print(parallelepipede1.perimetre()) # 16
print(parallelepipede1.surface()) # 15
print(Parallelepipede)