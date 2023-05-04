ann = {"Arthur": ["Arthur Chevrel", "Rouen", "0783667851"]}

def add(annuaire):
    fname = input("Prénom: ")
    name = input("Nom: ")
    city = input("Ville: ")
    tel = input("Numéro tel: ")
    annuaire[fname] = [fname+" "+name, city, tel]
    
    return annuaire

def affiche(annuaire):
    print("Voici l'annuaire:\n", annuaire)

a = True
while a==True:   
    print("""\n-----MENU-----
1) Ajouter un élève
2) Afficher l'annuaire
3) Quitter
    """)
      
    ask = int(input("Que voulez-vous faire? : "))

    if ask == 1:
        ann = add(ann)
        print("Voici l'annuaire:\n", ann)
    
    elif ask == 2:
        affiche(ann)

    elif ask == 3:
        a = False
    
    else:
        print("Réponse invalide, relancement du programme...")

print("Fin du programme.")