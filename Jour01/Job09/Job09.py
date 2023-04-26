class Student:
    def __init__(self, nom, prenom, num_etudiant, credits=0):
        self._nom = nom
        self._prenom = prenom
        self._num_etudiant = num_etudiant
        self._credits = credits
        self._level = self._studentEval()
        
    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._studentEval()
            
    def get_credits(self):
        return self._credits
    
    def studentInfo(self):
        print(f"Nom : {self._nom}\nPrénom : {self._prenom}\nIdentifiant : {self._num_etudiant}\nNiveau : {self._level}")
    
    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
john_doe = Student("Doe", "John", 145)
john_doe.add_credits(80)
john_doe.studentInfo()

