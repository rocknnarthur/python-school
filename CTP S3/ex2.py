import PySimpleGUI as sg
from random import randint

layout = [[sg.Image(filename="zombietama_normal.png", key="base")],
[sg.Button("Balance un truc !!!")],
[sg.Image(filename="", key="objet")],
[sg.Text("", key="text")]]

window = sg.Window("Tama", layout)

a = True
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if a == True:
        if event == "Balance un truc !!!":
            n = randint(1,3)
            if n == 1:
                window["base"].update(filename="zombietama_gone.png")
                window["objet"].update(filename="bin.png")
                window["text"].update("Vous avez jeté une poubelle, la barrière s'est cassée...")
                a = False

            elif n == 2:
                window["base"].update(filename="zombietama_attack.png")
                window["objet"].update(filename="bone.png")
                window["text"].update("Vous avez jeté un os, mauvaise idée...")

            elif n == 3:
                window["base"].update(filename="zombietama_zen.png")
                window["objet"].update(filename="brain.png")
                window["text"].update("Vous avez jeté une cervelle, il a l'air calme...")

window.close()