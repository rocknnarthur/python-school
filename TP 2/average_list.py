def average_list(l):
    r=0
    for i in l:
        r += i
    r = r/len(l)
    return r

l = []
n = int(input("Donner un entier: "))
for k in range(1, n+1):
    l.append(k)
call = average_list(l)
print(f"La moyenne des n entiers est de {call}")