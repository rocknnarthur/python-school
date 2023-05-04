from math import ceil,pi

def aire_cercle(r):
    a = 0
    a = pi*(r**2)
    a = ceil(a)
    return a

r = int(input("Rayon de votre cercle: "))
call = aire_cercle(r)
print(f"L'aire de votre cercle est de {call}m²")