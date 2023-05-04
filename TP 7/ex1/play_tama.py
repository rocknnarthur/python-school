from tama import Tama
import PySimpleGUI as sg
from repeat import Repeat

dog = Tama()

def cycle():
    if dog.feed >= 30 and dog.happy >= 30:
        window["dog"].update(filename="dog_boy4.png")
        dog.vieillir()
    elif dog.est_mort():
        window["dog"].update(filename="tama_dead.png")
    elif dog.est_malheureux():
        dog.vieillir()
        window["dog"].update(filename="tama_unhappy.png")
    else:
        dog.vieillir()

    window["feed"].update(dog.feed)
    window["happy"].update(dog.happy)
    

layout = [[sg.Image(filename="dog_boy4.png", key="dog")], 
[sg.Image(filename="bowl1.png", enable_events=True, key="bowl"), sg.Text(dog.feed, key="feed"), sg.Button("Nourrir")], 
[sg.Image(filename="bone1.png", enable_events=True, key="bone"), sg.Text(dog.happy, key="happy"), sg.Button("Jouer")]]

window = sg.Window("Tama", layout, location=(0,0), element_padding=(20,0), margins=(0,0))

t = Repeat(1.0, cycle)
t.start()

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Nourrir":
        dog.nourrir()
    if event == "Jouer":
        dog.distraire()


t.cancel()
window.close()