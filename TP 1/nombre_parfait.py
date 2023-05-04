def n_parfait(n):
    l=[]
    for i in range(1, 1000):
        if n != i:
            if n%i == 0:
                l.append(i)
    r=0
    for j in l:
        r += j
    
    if r == n:
        return True
    else:
        return False

def cmb_parfait(a,b):
    l=[]
    for n in range(a, b+1):
        if n_parfait(n):
            l.append(n)
    return l

a = int(input("Entier a: "))
b = int(input("Entier b: "))

call = cmb_parfait(a, b)
print(f"Liste des nombres parfaits entre {a} et {b}: {call}")