import PySimpleGUI as sg

layout = [[sg.Text("Saisissez votre nom :")], [sg.Input(key ='-INPUT-')], [sg.Button("Valider")], [sg.Text(key='-OUTPUT-')]]

window = sg.Window("Bonjour", layout)

while True:
    event , values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Valider":
        window['-OUTPUT-'].update("Bonjour " + values['-INPUT-'] + " !")

window.close()
