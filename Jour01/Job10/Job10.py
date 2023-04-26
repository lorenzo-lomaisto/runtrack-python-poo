class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50
    
    def get_marque(self):
        return self.marque
    
    def set_marque(self, marque):
        self.marque = marque
    
    def get_modele(self):
        return self.modele
    
    def set_modele(self, modele):
        self.modele = modele
        
    def get_annee(self):
        return self.annee
    
    def set_annee(self, annee):
        self.annee = annee
    
    def get_kilometrage(self):
        return self.kilometrage
    
    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage
    
    def is_en_marche(self):
        return self.en_marche
    
    def demarrer(self):
        if self.verifier_plein() > 5:
            self.en_marche = True
            print("La voiture a démarré.")
        else:
            print("Le réservoir est presque vide, veuillez faire le plein.")
    
    def arreter(self):
        self.en_marche = False
        print("La voiture a été arrêtée.")
    
    def get_reservoir(self):
        return self.reservoir
    
    def set_reservoir(self, reservoir):
        self.reservoir = reservoir
    
    def verifier_plein(self):
        return self.reservoir
    
    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.kilometrage} km"
    

# Créer une instance de la classe "Voiture"
ma_voiture = Voiture("Toyota", "Corolla", 2015, 80000)

# Vérifier les attributs de la voiture
print(ma_voiture.get_marque()) # Toyota
print(ma_voiture.get_modele()) # Corolla
print(ma_voiture.get_annee()) # 2015
print(ma_voiture.get_kilometrage()) # 80000
print(ma_voiture.is_en_marche()) # False
print(ma_voiture.get_reservoir()) # 50

# Démarrer la voiture (doit afficher "La voiture a démarré.")
ma_voiture.demarrer()

# Vérifier si la voiture est en marche (doit afficher "True")
print(ma_voiture.is_en_marche())

# Arrêter la voiture (doit afficher "La voiture a été arrêtée.")
ma_voiture.arreter()

# Changer le kilométrage de la voiture
ma_voiture.set_kilometrage(85000)
print(ma_voiture.get_kilometrage()) # 85000

# Changer la quantité de carburant dans le réservoir
ma_voiture.set_reservoir(40)
print(ma_voiture.get_reservoir()) # 40

# Afficher la voiture en format chaîne de caractères


