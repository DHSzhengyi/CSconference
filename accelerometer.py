from microbit import *
while True:
    reading = accelerometer.get_x()
    """ while you're at it, try get_y() and get_z() ;) """
    if reading > 20:
        display.show("L")
    elif reading < -20:
        display.show("R")
    else:
        display.show("-")
