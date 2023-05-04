import PySimpleGUI as sg

def add(name, num):
    d[name] = num
    window["dic"].update(d)

def liste(l):
    for key in d.keys():
        a = 0
        l.append(sg.Text(f"{key}", enable_events=True, key=f"{a}"))
        a += 1

d={"arthur chevrel": "0783667851"}
l=[]

liste(l)

layout = [[l],
[sg.Text("Ajouter un contact:"), sg.Input(key="nom"), sg.Input(key="tel"), sg.Button("Ajouter")]]

window = sg.Window("Annuaire", layout, location=(0,0), element_padding=(10,20), margins=(0,0))

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Ajouter":
        name = values["nom"]
        num = values["tel"]
        add(name, num)



window.close()