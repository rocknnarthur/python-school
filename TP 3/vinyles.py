class vinyle:
    def __init__(self, title, artist, rate, release):
        self.titre = title
        self.nom = artist
        self.note = rate
        self.year = release

    def afficher(self):
        print(f"\nVinyle:\nTitre: {self.titre}\nArtiste: {self.nom}\nNote: {self.note}/5\nParution: {self.year}")


def add_vinyle(l):
    title = input("Titre du vinyle: ")
    artist = input("Artiste du vinyle: ")
    rate = 0
    while rate < 1 or rate > 5:
        rate = int(input("Note du vinyle ( /5): "))
    release = int(input("Date de sortie du vinyle: "))
    v = vinyle(title, artist, rate, release)
    l.append(v)
    return l

def vinyles_artist(l, name):
    for v in l:
        if v.nom == name:
            v.afficher()

def vinyles_year(l, annee):
    for v in l:
        if v.year == annee:
            v.afficher()

def vinyles_artist_m(l, name):
    l2 = []
    r = 0
    b = 0
    for v in l:
        if v.nom == name:
            r += v.note
            b += 1
            l2.append(v)
    r /= b
    for v1 in l2:
        if v1.note > r:
            v1.afficher()

l=[]

a = True
while a == True:
    print("""=====MENU=====
1) Ajouter un vinyle
2) Afficher les vinyles d'un artiste
3) Afficher les vinyles d'une année
4) Afficher les vinyles > à la moy.
5) Quitter
    """)

    ask = int(input("Faites un choix [1,2,3,4 ou 5]: "))

    if ask == 1:
        l = add_vinyle(l)

    elif ask == 2:
        name = input("Nom de l'artiste: ")
        vinyles_artist(l, name)

    elif ask == 3:
        year = int(input("Année de parution: "))
        vinyles_year(l, year)

    elif ask == 4:
        name = input("Nom de l'artiste: ")
        vinyles_artist_m(l, name)

    elif ask == 5:
        a = False

    else:
        print("Choix invalide, réessayez")

print("Programme terminé.")