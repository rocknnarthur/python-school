class Coureur:
    def __init__(self, nom, prenom, distance, temps):
        self.name = nom
        self.fname = prenom
        self.d = distance
        self.t = temps
    
    def afficher(self):
        print(f"{self.name}, {self.fname}, {self.d}, {self.t}")

    def new_time(self, t2):
        if t2 < self.t:
            self.t = t2
        elif t2 == self.t:
            print("même temps")
        else:
            print("le temps 1 reste le meilleur.")