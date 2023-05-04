class Voilier:
    def __init__(self, nom, longueur, voilure):
        self.name = nom
        self.long = longueur
        self.voile = voilure
    
    def afficher(self):
        print(f"Voilier:\nNom:{self.name}\nTaille:{self.long}m\nVoilure:{self.voile} voiles")

    def comparer(self, v2):
        r1 = self.voile/self.long
        r2 = v2.voile/v2.long
        if r1 > r2:
            return Voilier(self.name, self.long, self.voile)
        elif r1 == r2:
            return Voilier(self.name, self.long, self.voile)
        else:
            return v2

class Visiteur:
    def __init__(self, nom, pvisites):
        self.name = nom
        self.dico = pvisites    #clé: numéro du jour, valeur: liste de bateaux à visiter ce jour (clé)

    def ajouter_bateau(self, jour, bateau):
        if jour not in self.dico:
            self.dico[jour] = [bateau]
            return True
        else:
            if len(self.dico[jour]) < 3:
                self.dico[jour].append(bateau)
                return True
            else:
                return False

    def meilleur_voilier_par_jour(self):
        d={}
        for j,lv in self.dico.items():
            l=[]
            for v in lv:
                l.append(v)
            if len(l) == 3:
                a = l[0].comparer(l[1]).comparer(l[2])
                d[j] = a.name
            elif len(l) == 2:
                a = l[0].comparer(l[1])
                d[j] = a.name
            else:
                d[j] = l[0].name
        return d

#programme test
v1 = Voilier("bato", 100, 3)
v2 = Voilier("vogue merry", 200, 5)
v3 = Voilier("piti bato", 50, 2)
vis1 = Visiteur("Luffy", {1:[v1,v2], 2:[v1], 3:[v1,v2,v3]})

print("\nAjout d'un bateau")
j = int(input("Jour pour visite: "))
name = input("Nom du voilier: ")
long = int(input("Longueur voilier (en m): "))
nvoile = int(input("Nbr de voiles: "))
b = Voilier(name, long, nvoile)

if not vis1.ajouter_bateau(j, b):
    print("ajout impossible (nbr de visites max atteint)")

print("\nDictionnaire des meilleurs bateaux par jour:")
print(vis1.meilleur_voilier_par_jour())