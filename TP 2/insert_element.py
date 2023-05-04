def insert_e(l, e, i):
    i -= 1
    l = l[:i] + [e] + l[i:]
    return l

l=[1,5,10,15,20]
e = int(input("Entrez un nombre: "))
i = int(input("Entrez un indice: "))

call = insert_e(l, e, i)
print(call)