from datetime import datetime
from repeat import Repeat
import time
import PySimpleGUI as sg

# 17/12/2022 0:00 (Vacances de Noël)

def timeuntilchristmas():
    now = datetime.now()
    christmas = datetime.strptime("17/12/22 00:00:00", "%d/%m/%y %H:%M:%S")
    gap = christmas - now
    return gap

print(f"Il reste {timeuntilchristmas()} avant les vacances de Noël.")


t = Repeat(1.0, timeuntilchristmas)
t.start()


layout = [[sg.Text(timeuntilchristmas())]]

window = sg.Window("Countdown", layout)


while True:
    event , values = window.read()
    time.sleep(1)
    t.cancel()
    
    if event == sg.WINDOW_CLOSED:
        break

window.close()