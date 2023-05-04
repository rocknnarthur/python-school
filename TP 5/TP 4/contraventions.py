class Infraction:
    def __init__(self, libelle, tarif):
        self.motif = libelle
        self.montant = tarif

    def afficher(self):
        print(f"Infraction:\nLibellé:{self.motif}\nTarif:{self.montant}€")

class Conducteur:
    def __init__(self, nom, prenom, numero):
        self.name = nom
        self.fname = prenom
        self.npermis = numero
    
    def afficher(self):
        print(f"Conducteur:\nNom:{self.name}\nPrénom:{self.fname}\nNuméro de Permis:{self.npermis}")

class ProcesVerbal:
    def __init__(self, numPV, driverPV, listInfrac):
        self.numPV = numPV
        self.driverPV = driverPV
        self.l = listInfrac
    
    def afficher(self):
        print(f"PV:\nNuméro PV:{self.numPV}\nConducteur verbalisé:{self.driverPV.name} {self.driverPV.fname}\nListe des infractions:{self.l}")

    def montantTotal(self):
        t = 0
        for p in self.l:
            t += p.montant
        return t
    
    def infractionMax(self):
        best = None
        best_n = 0
        for e in self.l:
            if e.montant > best_n:
                best_n = e.montant
                best = e

        print("\nInfraction la plus chère:\n")
        best.afficher()


def sommeParConducteur(lPV):
    dico={}
    for pv in lPV:
        np = pv.driverPV.npermis
        st = pv.montantTotal()
        if np in dico:
            dico[np] += st
        else:
            dico[np] = st

    return dico

#programme test
inf1 = Infraction("Crotte sur la voie publique",5)
inf11 = Infraction("MMA avec un ours",60000)
inf2 = Infraction("Pet sur un officier de police",50)
inf22 = Infraction("Vol à pieds armés",15000)
inf3 = Infraction("Tirage de langue à un passant",2)
inf33 = Infraction("Deal de HandSpinner",99000)
lInf1 = [inf1, inf11]
lInf2 = [inf2, inf22]
lInf3 = [inf3, inf33]
c1 = Conducteur("Depardieu", "Gérard", 69)
c2 = Conducteur("Pratt", "Chris", 8)
c3 = Conducteur("Johnson", "Dwayne", 100)
pv1 = ProcesVerbal(1, c1, lInf1)
pv2 = ProcesVerbal(2, c2, lInf2)
pv3 = ProcesVerbal(3, c3, lInf3)
lPV = [pv1, pv2, pv3]

print(sommeParConducteur(lPV))
pv1.infractionMax()
pv2.infractionMax()
pv3.infractionMax()
