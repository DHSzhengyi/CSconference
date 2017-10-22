from microbit import *
import random

flash = [Image().invert()*(x/9) for x in range(9, -1 , -1)]

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('flash')
    
    incoming = radio.receive()
    if incoming == 'flash':
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        
        if random.randint(0,5) == 2:
            sleep(500)
            radio.send('flash')
