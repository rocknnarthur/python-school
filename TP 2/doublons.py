def erase_double(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2
n = int(input("Combien de nombres voulez-vous écrire?: "))

l=[]
a=0
while a!=n:
    k = int(input("Entrez un nombre: "))
    l.append(k)
    a += 1

call = erase_double(l)
print(f"La liste sans doublons: {call}")