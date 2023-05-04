from datetime import datetime
from repeat import Repeat
import time

# 17/12/2022 0:00 (Vacances de Noël)

def timeuntilchristmas():
    now = datetime.now()
    christmas = datetime.strptime("16/12/23 00:00:00", "%d/%m/%y %H:%M:%S")
    gap = christmas - now
    print(f"Il reste {gap} avant les vacances de Noël.")


t = Repeat(3.0, timeuntilchristmas)
t.start()
time.sleep(7)
t.cancel()
