def t2(t1, d1, d2):
    if d1 > 0:
        t2 = t1*(d2/d1)*1.06
        return t2
    else:
        return 0

t1 = float(input("Votre temps de référence (en min): "))
d1 = float(input("Votre distance de référence (en km): "))
d2 = float(input("Votre distance sur la course à prédire (en km): "))
call = t2(t1, d1, d2)
print(f"Votre temps de prédiction est de {call}min")