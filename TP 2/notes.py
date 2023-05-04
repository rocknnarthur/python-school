def ask(d):
    name = input("Nom de l'élève: ")
    note = float(input("Note: "))
    d[name] = note
    return d

d={}
for i in range(1, 6):
    d = ask(d)

r=0
for value in d.values():
    r += value
r /= 5

print(d)
print(f"La moyenne de la classe est de {r}")