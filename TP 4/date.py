class Date:
    def __init__(self, jour, mois, annee):
        self.d = jour
        self.m = mois
        self.y = annee

    def afficher(self, lang):
        day = self.d
        month = self.m
        if lang == "US":
            if self.d < 10:
                day = "0" + str(self.d)
            if self.m < 10:
                month = "0" + str(self.m)
            text = f"{month}-{day}-{self.y}"
        
        else:
            if self.d < 10:
                day = "0" + str(self.d)
            if self.m < 10:
                month = "0" + str(self.m)
            text = f"{day}/{month}/{self.y}"
        return text

    def est_plus_grande(self, date):
        if self.y < date.y:
            return True

        elif self.y == date.y:
            if self.m < date.m:
                return True

            elif self.m == date.m:
                if self.d < date.d:
                    return True

                elif self.d == date.d:
                    return "same"

                else:
                    return False

            else:
                return False

        else:
            return False

class Personne:
    def __init__(self, nom, prenom, nation, bdate):
        self.name = nom
        self.fname = prenom
        self.nat = nation
        self.birth = bdate

    def afficher(self):
        print(f"\nNom: {self.name}\nPrénom: {self.fname}\nNationalité: {self.nat}\nDate de naissance: {self.birth.afficher(self.nat)}")
        
    def est_plus_jeune(self, pers):
        if self.birth.y > pers.birth.y:
            return True

        elif self.birth.y == pers.birth.y:
            if self.birth.m > pers.birth.m:
                return True

            elif self.birth.m == pers.birth.m:
                if self.birth.d > pers.birth.d:
                    return True

                elif self.birth.d == pers.birth.d:
                    return "same"

                else:
                    return False

            else:
                return False

        else:
            return False

#programme test
name = input("Votre nom?: ")
fname = input("Votre prénom?: ")
nat = input("Quelle est votre nationalité? [US/autre]: ")
d = int(input("Entrer le jour: "))
m = int(input("Entrer le mois: "))
y = int(input("Entrer l'année: "))

date = Date(d, m, y)

p = Personne(name, fname, nat, date)
p.afficher()

print("\nAutre date:")
d = int(input("Entrer le jour: "))
m = int(input("Entrer le mois: "))
y = int(input("Entrer l'année: "))
date2 = Date(d, m, y)

if date.est_plus_grande(date2):
    print("La 1ère date est plus ancienne que l'autre.")
elif not date.est_plus_grande(date2):
    print("La 2ème date est plus ancienne que l'autre.")
else:
    print("Les 2 dates sont identiques.")

print("\nAutre personne:")
name = input("Votre nom?: ")
fname = input("Votre prénom?: ")
nat = input("Quelle est votre nationalité? [US/autre]: ")
p2 = Personne(name, fname, nat, date2)

if p.est_plus_jeune(p2):
    print(f"{p.fname} est plus jeune.")
elif not p.est_plus_jeune(p2):
    print(f"{p2.fname} est plus jeune.")
else:
    print("Les deux personnes ont le même âge.")