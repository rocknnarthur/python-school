import PySimpleGUI as sg

layout = [[sg.Image(filename="question.gif", enable_events=True, key="Image1"), sg.Image(filename="question.gif", enable_events=True, key="Image2")], [sg.Image(filename="question.gif", enable_events=True, key="Image3"), sg.Image(filename="question.gif", enable_events=True, key="Image4")]]

window = sg.Window("Démineur", layout, location=(0,0), element_padding=(0,0), margins=(0,0))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Image1":
        window["Image1"].update(filename="bombe.gif")
    elif event == "Image2":
        window["Image2"].update(filename="bombe.gif")
    elif event == "Image3":
        window["Image3"].update(filename="win.gif")
    elif event == "Image4":
        window["Image4"].update(filename="bombe.gif")

window.close()