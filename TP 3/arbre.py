class arbre:
    def __init__(self):
        self.taille = 0
        self.age = 0

    def print_stats(self):
        print(f"Taille: {self.taille}m\nAge: {self.age}ans")

    def growth(self, t):
        self.age += 1
        self.taille += t

t = float(input("De combien voulez-vous faire grandir l'arbre ? (en m): "))
print("\nArbre:")
a = arbre()
a.growth(t)
a.print_stats()