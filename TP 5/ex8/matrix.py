import numpy as np



#matrices
print("Création des 2 matrices:")
print("Matrice 1:")
a = int(input("Entrez l'entier a:"))
b = int(input("Entrez l'entier b:"))
c = int(input("Entrez l'entier c:"))
d = int(input("Entrez l'entier d:"))
m1 = np.matrix([[a, b], [c, d]])

print("Matrice 2:")
a = int(input("Entrez l'entier a:"))
b = int(input("Entrez l'entier b:"))
c = int(input("Entrez l'entier c:"))
d = int(input("Entrez l'entier d:"))
m2 = np.matrix([[a, b], [c, d]])

#opérations matricielles
ms = m1.__add__(m2)
mp = np.dot(m1,m2)

#affiche somme
print(f"{m1} \n+ \n{m2} \n= \n{ms}\n")

#affiche produit
print(f"{m1} \n* \n{m2} \n= \n{mp}")