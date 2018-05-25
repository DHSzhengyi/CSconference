from microbit import *
while True:
    reading = accelerometer.get_x()
    """ while you're at it, try get_y() and get_z() ;) """
    if reading > 40:
        display.show("R")
    elif reading < -40:
        display.show("L")
    else:
        display.show("-")
