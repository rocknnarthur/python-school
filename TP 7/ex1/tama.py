class Tama:
    def __init__(self):
        self.happy = 100
        self.feed = 100

    def affiche(self):
        print(f"Nourriture:{self.feed}\nBonheur:{self.happy}")

    def est_malheureux(self):
        if self.happy<30 or self.feed<30:
            return True
        else:
            return False
        
    def est_mort(self):
        if self.happy == 0 or self.feed == 0:
            return True
        else:
            return False

    def nourrir(self):
        if self.feed == 0 or self.happy == 0:
            print("Tama est mort, donc ne mange pas.")

        elif self.feed <= 95:
            self.feed += 5
        
        else:
            print("Tama n'a pas faim, il a assez mangé.")

    def distraire(self):
        if self.feed == 0 or self.happy == 0:
            print("Tama est mort, donc ne bouge pas.")

        elif self.happy <= 97:
            self.happy += 3
        
        else:
            print("Tama n'a pas envie de jouer, il a assez dépensé.")

    def vieillir(self):
        if self.feed != 0 and self.happy != 0:
            self.happy -= 1
            self.feed -= 1
        
        else:
            print("Tama est mort, donc ne vieillit pas.")