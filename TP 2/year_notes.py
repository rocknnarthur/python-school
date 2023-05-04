#fonctions
def fill_notes(dic, ds):
    if ds not in dic:
        dic[ds] = []
    name = ""
    while not name == "-1":
        name = input("Nom de l'élève: ")
        if name != "-1":
            note = float(input("Note de l'élève: "))
            dic[ds].append([name, note])
    print("Remplissage terminé.")
    return dic

def print_ds(dic, ds):
    if dic == {}:
        print("Dictionnaire vide.")
    elif ds not in dic:
        print("Erreur, DS non effectué")
    else:
        print(dic[ds])

def average_year(dic):
    a = 0
    b = 0
    for ds, couple in dic.items():
        for note in couple:
            a += note[1]
            b += 1
    a /= b
    return a

def average_student(dic, name):
    a = 0
    b = 0
    for ds, couple in dic.items():
        for note in couple:
            if note[0] == name:
                a += note[1]
                b += 1
    a /= b
    return a


#menu
d = {}

x = True
while x == True:
    print("""\n-----MENU-----
1) Remplir les notes d'un DS
2) Afficher les notes d'un DS
3) Calculer la moyenne G de l'année
4) Calculer la moyenne G d'un élève
5) Afficher le dico principal
6) Quitter
    """)

    ask = int(input("Faites un choix: "))

    if ask == 1:
        id = input("Nom du DS: ")
        d = fill_notes(d, id)

    elif ask == 2:
        id = input("Nom du DS: ")
        d = print_ds(d, id)

    elif ask == 3:
        if d != {}:
            print(average_year(d))
        else:
            print("Dictionnaire vide.")

    elif ask == 4:
        if d != {}:
            n = input("Entrez le nom de l'élève: ")
            print(average_student(d, n))
        else:
            print("Dictionnaire vide.")
    elif ask == 5:
        print(d)

    elif ask == 6:
        x = False

    else:
        print("Erreur de choix, recommencez")

print("Programme terminé.")