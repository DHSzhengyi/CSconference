from microbit import *
from random import randint 

"""reading = pin0.read_analog()//204

# utilising microbit library. display is off by default.
for i in range(5):
    display.set_pixel(readng,i, 9) # light up the wall

# battleship with 2 players!
radio.on()
# tune in to your friend's microbit! be wary of signal interference.
radio.config(length=251,queue=3,channel=5,power=6,,,,)
"""
# board setup
com_board = [[0 for i in range (5)] for j in range(5)]

#display.scroll("Battleships")
while not button_a.is_pressed(): # the moment button a is pressed, loop is broken
    display.scroll("Hold A to start") # note that loop does not run again until after scroll.
    # thus, button a needs to be pressed down when the loop restarts (hold)
    
# computer places two ships randomly.
com_board[randint(0,4)][randint(0,4)] = 1
com_board[randint(0,4)][randint(0,4)] = 1

display.scroll("Game start!")
display.show(Image.HEART)
sleep(200)
display.clear()

# now, for the fun part!
player_points = 0
current = 0
#player has 20 turns to win    
for _ in range(20):
    #win
    if player_points == 2:
        break
    x_coord = 0 # left
    y_coord = 0 # top
    while True:
        display.set_pixel(x_coord, y_coord, 9)
        # attack a ship with A and B! use A or B to navigate!
        # note that turns are based on whoever's playing!
        if button_a.is_pressed() and button_b.is_pressed():
            # attack the square! 
            # missed
            if com_board[y_coord][x_coord] == 0:
                display.set_pixel(x_coord, y_coord, 2)
                sleep(3000)
            else:#com_board[y_coord][x_coord] = 2
                #hit ship
                display.set_pixel(x_coord, y_coord, 9)
                player_points += 1
                sleep(1000) 
            break

        elif button_a.is_pressed() or button_b.is_pressed():
            display.set_pixel(x_coord, y_coord, current)
            if button_a.is_pressed():
                x_coord = (x_coord + button_a.get_presses()) % 5 # cycles back
            else: # button_b.is_pressed()
                y_coord = (y_coord - button_b.get_presses()) % 5 # likewise
            current = display.get_pixel(x_coord,y_coord)

# whew, so now the loop's broke. the game has ended.
if player_points == 2:
    display.scroll("Player wins!")
else: # computer won
    display.scroll("Computer wins!")
