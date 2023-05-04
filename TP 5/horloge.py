from datetime import datetime
import time

def today_date():
    print("Nous sommes le", datetime.today().strftime("%d-%m-%Y"))

def today_time():
    print("Il est", datetime.today().strftime("%H:%M"))

def today_dateNtime():
    print("Nous sommes le", datetime.today().strftime("%d-%m-%Y et il est %H:%M"))



a = True
while a == True:
    print("""\n========MENU========
1) Date d'aujourd'hui
2) Heure courante
3) Les deux
4) Quitter
    """)

    ask = int(input("Faites un choix [1,2,3 ou 4]: "))

    if ask == 1:
        today_date()
        time.sleep(2)

    elif ask == 2:
        today_time()
        time.sleep(2)

    elif ask == 3:
        today_dateNtime()
        time.sleep(2)

    elif ask == 4:
        a = False

    else:
        print("Mauvais numéro, réessayez.")
        time.sleep(2)

print("Programme terminé.")