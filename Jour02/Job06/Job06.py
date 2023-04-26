class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele
        
    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modele :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)
        
        
    def demarrer(self):
        print("Attention, je roule.")
        

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)
        
    def demarrer(self):
        print("Vroum vroum ! Let's go for a ride !")
        
        
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roues)
        
    def demarrer(self):
        print("Brrrrrrr ! Let's hit the road !")
        

# Instanciation et utilisation des objets

# Voiture
ma_voiture = Voiture("Mercedes", "Classe A", 2020, 18500, 5)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

# Moto
ma_moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
ma_moto.informationsVehicule()
ma_moto.demarrer()













