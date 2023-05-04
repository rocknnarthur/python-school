n = int(input("Combien avez-vous d'articles?: "))
l1 = []
l2 = []

for a in range(1, n+1):
    prix_ht = 0
    prix_tt = 0
    qte = int(input(f"Quelle quantité pour l'article {a} ?: "))
    prix_ht = float(input("Le prix hors taxe?: "))
    prix_ht = qte*prix_ht
    l1.append(prix_ht)
    ask_tva = input("TVA réduite pour cette article? [oui/non]: ")
    if ask_tva == "oui":
        prix_tt = prix_ht + (prix_ht*0.055)
    else:
        prix_tt = prix_ht + (prix_ht*0.2)
    l2.append(prix_tt)
    
print("""=======================================
          TICKET DE CAISSE
""")

pht = 0
ptt = 0
for i in range(1, n+1):
    print(f"Article {i}: Prix HT: {l1[i-1]}, Prix TT: {l2[i-1]}")
    pht += l1[i-1]
    ptt += l2[i-1]

print(f"Total HT: {pht}, Total TT: {ptt}")
    
    