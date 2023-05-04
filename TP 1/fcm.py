def fcm(age):
    
    fcm = 192 - 0.007 * (age**2)
    return fcm
age = 0
while age < 1:
    age = int(input("Saisir votre âge: "))
    if age < 1:
        print("Valeur positive requise, recommencez !")
call = fcm(age)
print(f"Votre FCM est de {call} bpm")