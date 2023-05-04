import PySimpleGUI as sg

layout = [[sg.Text("Bonjour !")]]

window = sg.Window("Fenêtre", layout)

event, values = window.read()

window.close()