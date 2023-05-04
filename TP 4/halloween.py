class Friandise:
    def __init__(self, nom, poids, note):
        self.name = nom
        self.p = poids
        self.rate = note

class Bol:
    def __init__(self, pmax, l_friandises):
        self.max = pmax
        self.l = l_friandises

    def prendre_meilleure_friandise(self):
        best = None
        best_n = 0
        for e in self.l:
            if e.rate > best_n:
                best_n = e.rate
                best = e
        a = 0
        for e in self.l:
            if e == best:
                del(self.l[a])
                print(f"Friandise retirée:\n{best.name}\nNote: {best.rate}/10")

            a += 1
        
    
    def ajouter_friandise(self):
        if self.max == len(self.l):
            return False
        else:
            return True

    def calculer_moyenne(self, boolean):
        moy = 0
        div = 0
        if not boolean:
            for e in self.l:
                moy += e.rate
            moy /= len(self.l)
            return moy
        else:
            for e in self.l:
                moy += (e.p*e.rate)
                div += e.p
            moy /= div
            return moy

#programme test (menu)
l = []
pmax = int(input("Contenance max du bol: "))
bol = Bol(pmax, l)
boolean = int(input("Pondérée = 1 sinon 0 ou autre: "))
if boolean == 1:
    boolean = True
else:
    boolean = False

a = True
while a == True:
    print("""=====MENU=====
1) Ajouter une friandise au bol
2) Prendre meilleure friandise
3) Calculer la moyenne
4) Pondérée ou non
5) Quitter
    """)

    ask = int(input("Faites un choix [1,2,3,4 ou 5]: "))

    if ask == 1:
        name = input("Nom de la friandise: ")
        p = int(input("Poids de la friandise: "))
        note = 11
        while note > 10 or note < 0:
            note = int(input("Note de la friandise (/10): "))
        fd = Friandise(name, p, note)
        if bol.ajouter_friandise():
            bol.l.append(fd)
        else:
            print("Pas assez de place dans le bol.")

    elif ask == 2:
        bol.prendre_meilleure_friandise()

    elif ask == 3:
        if boolean:
            typ = "pondérée"
        else:
            typ = "normale"
        print(f"Vous avez choisi une moyenne {typ}")
        print(f"La moyenne est de {bol.calculer_moyenne(boolean)}")

    elif ask == 4:
        boolean = int(input("Pondérée = 1 sinon 0 ou autre: "))
        if boolean == 1:
            boolean = True
        else:
            boolean = False

    elif ask == 5:
        a = False

    else:
        print("Choix invalide, réessayez")

print("Programme terminé.")
