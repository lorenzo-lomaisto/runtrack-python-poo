import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        for couleur in ["Pique", "Coeur", "Carreau", "Trèfle"]:
            for valeur in range(2, 11):
                self.paquet.append(Carte(valeur, couleur))
            for valeur in ["Valet", "Dame", "Roi"]:
                self.paquet.append(Carte(10, couleur))
            self.paquet.append(Carte(1, couleur))
            self.paquet.append(Carte(11, couleur))
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

class Joueur:
    def __init__(self):
        self.main = []

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def total_main(self):
        total = sum([carte.valeur for carte in self.main])
        nb_as = sum([carte.valeur in [1, 11] for carte in self.main])
        while total <= 11 and nb_as > 0:
            total += 10
            nb_as -= 1
        return total

class JeuBlackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.joueur = Joueur()
        self.croupier = Joueur()

    def jouer(self):
        # Distribution des cartes
        for i in range(2):
            self.joueur.ajouter_carte(self.jeu.tirer_carte())
            self.croupier.ajouter_carte(self.jeu.tirer_carte())

        # Tour du joueur
        while self.joueur.total_main() < 21:
            print("Main joueur:", [carte.valeur for carte in self.joueur.main])
            choix = input("Voulez-vous tirer une carte (T) ou passer (P) ? ").upper()
            if choix == "T":
                self.joueur.ajouter_carte(self.jeu.tirer_carte())
            elif choix == "P":
                break

        # Tour du croupier
        while self.croupier.total_main() < 17:
            self.croupier.ajouter_carte(self.jeu.tirer_carte())

        # Résultats
        print("Main joueur:", [carte.valeur for carte in self.joueur.main])
        print("Total joueur:", self.joueur.total_main())
        print("Main croupier:", [carte.valeur for carte in self.croupier.main])
        print("Total croupier:", self.croupier.total_main())
        if self.joueur.total_main() > 21:
            print("Le joueur a dépassé 21, le croupier gagne.")
        elif self.croupier.total_main() > 21:
            print("Le croupier a dépassé 21, le joueur gagne.")
        elif self.joueur.total_main() > self.croupier.total_main():
            print("Le joueur gagne.")
        elif self.joueur.total_main() < self.croupier.total_main():
            print("Le croupier gagne.")
        else:
            print("Match nul.")

# Exemple d'utilisation
partie = JeuBlackjack()
partie.jouer()