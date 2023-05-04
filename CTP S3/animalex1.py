class Animal:
    def __init__(self, nom, espece, genre):
        self.name = nom
        self.esp = espece
        self.gender = genre

    def afficher(self):
        print(f"Nom: {self.name}\nEspèce: {self.esp}\nGenre: {self.gender}\n")