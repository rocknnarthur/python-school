from animalex1 import Animal

def ajouter(d):
    name = input("Nom de l'animal: ")
    esp = input("Espèce de l'animal: ")
    gender = input("Genre de l'animal: ")
    fence = input("Nom de l'enclos: ")

    if fence not in d:
        d[fence] = [Animal(name, esp, gender)]
    else:
        d[fence].append(Animal(name, esp, gender))


def afficher(d):

    for key in d.keys():
        print(f"{key}:")
        a=0
        for value in d[key]:
            value.afficher()
            a+=1
        print(f"Il y a {a} animaux dans l'enclos")

def diffespenclos(d):

    l=[]
    for key in d.keys():
        ltest=[]
        b=True
        for value in d[key]:
            if value.esp not in ltest:
                ltest.append(value.esp)
            else:
                b=False
        if b==True:
            l.append(key)
    return l



d={}

c=True
while c==True:
    print("""\n---Menu---
Que souhaitez vous faire?
1. Ajouter un animal
2. Afficher les enclos et les animaux
3. Afficher les enclos contenant espèces différentes
Autre touche pour quitter
    """)

    ask = int(input("Faites un choix: "))

    if ask == 1:
        ajouter(d)
    elif ask == 2:
        afficher(d)
    elif ask == 3:
        print(diffespenclos(d))
    else:
        c = False
    
print("programme terminé")