l = []
for note in range(1, 4):
    n = float(input(f"Saisissez votre note {note}: "))
    l.append(n)

a = 0
if l[0] >= 10 and l[1] >= 10 and l[2] >= 10:
    print("Année validée avec 10 au minimum partout")

elif l[0] < 8 or l[1] < 8 or l[2] < 8:
    print(f"Vous redoublez ayant une UE inférieure à 8")
    
elif (l[0] + l[1] + l[2])/3 >= 10:
    print("Année validée par moyenne > 10")
    
else :
    m = 0
    if l[0] < 10:
        m += 10 - l[0]
    if l[1] < 10:
        m += 10 - l[1]
    if l[2] < 10:
        m += 10 - l[2]
    print(f"Vous redoublez, il vous manque {m} points ")