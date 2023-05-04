import PySimpleGUI as sg
from math import ceil,pi

def aire_cercle(r):
    a = 0
    a = pi*(r**2)
    a = ceil(a)
    return a



layout = [[sg.Text("Saisissez le rayon du cerle en cm:")], [sg.Input(key ='-INPUT-')], [sg.Button("Valider")], [sg.Text(key='-OUTPUT-')]]

window = sg.Window("Bonjour", layout)

while True:
    event , values = window.read()
    r = int(values['-INPUT-'])

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Valider":
        window['-OUTPUT-'].update("Aire = " + str(aire_cercle(r)) + " cm²")

window.close()