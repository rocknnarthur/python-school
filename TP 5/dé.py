import random as rdm

l = []
a = 0
while a!=10000:
    n = rdm.randint(1,6)
    l.append(n)
    a += 1

u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
for e in l:
    if e == 1:
        u+= 1
    elif e == 2:
        v+= 1
    elif e == 3:
        w+= 1
    elif e == 4:
        x+= 1
    elif e == 5:
        y+= 1
    elif e == 6:
        z+= 1

print(f"Nombre de tirages de chaque numéros du dé:\n1: {u}, soit {(u/len(l))*100}%\n2: {v}, soit {(v/len(l))*100}%\n3: {w}, soit {(w/len(l))*100}%\n4: {x}, soit {(x/len(l))*100}%\n5: {y}, soit {(y/len(l))*100}%\n6: {z}, soit {(z/len(l))*100}%")

# Plus on augmente les tirages, plus les chances d'obtenir une des 6 faces équivalent aux autres.
# (soit environ 16,666666667% de chances pour chaque face)