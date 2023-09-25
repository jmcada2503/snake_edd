from getkey import getkey, keys
from threading import Thread
import time

while True:
    x = getkey()
    if (x == keys.UP):
        print("flecha arriba")
    if (x == keys.DOWN):
        print("flecha abajo")
    if (x == keys.LEFT):
        print("flecha izquieda")
    if (x == keys.RIGHT):
        print("flecha derecha")
    print("serpiente")
    time.sleep(0.2)
