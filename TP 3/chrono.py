import time as t

class chrono:
    def __init__(self):
        self.time = 0

    def demarrer(self):
        self.time = t.time()

    def afficher_t_ecoule(self):
        if self.time == 0:
            print("Chronomètre non lancé")
        else:
            tps = t.time() - self.time
            print(f"Temps écoulé: {tps}s")

c1 = chrono()
c1.demarrer()
t.sleep(2)
c1.afficher_t_ecoule()