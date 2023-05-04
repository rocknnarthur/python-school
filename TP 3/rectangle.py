class rectangle:
    def __init__(self, long, large):
        self.longueur = long
        self.largeur = large

    def calculerSurface(self):
        s = self.longueur*self.largeur
        return s

print("\nRectangle 1:")
long = int(input("Définir une longueur: "))
large = int(input("Définir une largeur: "))
r1 = rectangle(long, large)
s1 = r1.calculerSurface()

print("\nRectangle 2:")
long = int(input("Définir une longueur: "))
large = int(input("Définir une largeur: "))
r2 = rectangle(long, large)
s2 = r2.calculerSurface()

print("\nRectangle 3:")
long = int(input("Définir une longueur: "))
large = int(input("Définir une largeur: "))
r3 = rectangle(long, large)
s3 = r3.calculerSurface()


if (s1 and s2) > s3:
    print(f"Les rectangles 1 et 2 ont la plus grande surface avec {s1} m².")

elif (s1 and s3) > s2:
    print(f"Les rectangles 1 et 3 ont la plus grande surface avec {s1} m².")

elif (s2 and s3) > s1:
    print(f"Les rectangles 2 et 3 ont la plus grande surface avec {s2} m².")

elif s1 > (s2 and s3):
    print(f"Le rectangle 1 a la plus grande surface avec {s1} m².")

elif s2 > (s1 and s3):
    print(f"Le rectangle 2 a la plus grande surface avec {s2} m².")

elif s3 > (s1 and s2):
    print(f"Le rectangle 3 a la plus grande surface avec {s3} m².")

else:
    print(f"Les 3 rectangles ont la même surface avec {s1} m².")