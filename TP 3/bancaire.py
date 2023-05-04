class compte:
    def __init__(self, nom, dcv):
        self.titulaire = nom
        self.solde = 0
        self.decouvert_autorise = dcv

    def crediter(self, montant):
        self.solde += montant

    def debiter(self, montant):
        if not self.decouvert_autorise:
            if self.solde - montant >= 0:
                self.solde -= montant
                print("Débit accepté")
            else:
                print("Débit refusé")
        else:
            self.solde -= montant
    
    def afficher(self):
        print(f"\nCompte bancaire:\nNom du titulaire: {self.titulaire}\nSolde: {self.solde}€")

    def est_a_decouvert(self):
        if self.solde < 0:
            return True
        else:
            return False

name = input("Votre nom de titulaire ?: ")
dcv_ask = input("Autorisez-vous le découvert ? [oui/non]: ")
if dcv_ask == "oui":
    dcv = True
else:
    dcv = False
cpt = compte(name, dcv)

a = True
while a == True:
    print("""=====MENU=====
1) Créditer
2) Débiter
3) Afficher le nom et solde
4) Tester le découvert
5) Quitter
    """)

    ask = int(input("Faites un choix [1,2,3,4 ou 5]: "))

    if ask == 1:
        amount = float(input("Montant à créditer: "))
        cpt.crediter(amount)

    elif ask == 2:
        amount = float(input("Montant à débiter: "))
        cpt.debiter(amount)

    elif ask == 3:
        cpt.afficher()

    elif ask == 4:
        if cpt.est_a_decouvert():
            print(f"Compte à découvert avec {cpt.solde}€ !")
        else:
            print(f"Compte à couvert avec {cpt.solde}€")

    elif ask == 5:
        a = False

    else:
        print("Choix invalide, réessayez")

print("Programme terminé.")