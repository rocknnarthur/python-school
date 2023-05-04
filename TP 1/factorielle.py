n = int(input("Donnez un nombre: "))
result = 1
for i in range(1, n+1):
    result *= i
    
print(f"La factorielle de {n} est {result}")
    