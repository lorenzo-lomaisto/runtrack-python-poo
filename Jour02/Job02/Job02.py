class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        print("L'âge de la personne est :", self.age)
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
        
    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'un élève
eleve1 = Eleve()
eleve1.bonjour() # Hello
eleve1.allerEnCours() # Je vais en cours
eleve1.modifierAge(15) # Redéfinition de l'âge de l'élève à 15 ans
eleve1.affichageAge() # J'ai 15 ans

# Instanciation d'un professeur
professeur1 = Professeur("mathématiques")
professeur1.modifierAge(40) # Redéfinition de l'âge du professeur à 40 ans
professeur1.bonjour() # Hello
professeur1.enseigner() # Le cours va commencer