from microbit import *


"""reading = pin0.read_analog()//204

# utilising microbit library. display is off by default.
for i in range(5):
    display.set_pixel(readng,i, 9) # light up the wall

# battleship with 2 players!
radio.on()
# tune in to your friend's microbit! be wary of signal interference.
radio.config(length=251,queue=3,channel=5,power=6,,,,)
"""
# A: 1, C: 97, D: 139, E:  539, B: 51
# board setup
player_1_board = [[0 for i in range (5)] for j in range(5)]
player_2_board = [[0 for i in range (5)] for j in range(5)]

# ask the players to place ships. 2 ships.
display.scroll("Battleships")
while not button_a.is_pressed(): # the moment button a is pressed, loop is broken
    display.scroll("Hold A to start") # note that loop does not run again until after scroll.
    # thus, button a needs to be pressed down when the loop restarts (hold)

# placement cue. player 1.
display.scroll("Player 1 Place Ships")
# now microbit is handed over to player 1. player 1 uses this microbit to
# place ship. A goes right, B goes up, selector cycles back.
display.scroll("Press A and B together to place ship")

for i in range(2):
    # 2 ships.
    x_coord = 0 # left
    y_coord = 4 # bottom
    while True:
        display.set_pixel(x_coord, y_coord, 9) # show the selected tile
        if button_a.is_pressed() and button_b.is_pressed():
            # place ship. y coordinate accesses the row.
            if player_1_board[y_coord][x_coord] == 0: # just in case
                player_1_board[y_coord][x_coord] = 1
                display.set_pixel(x_coord, y_coord, 9)
                sleep(1000)
                break
            
        elif button_a.is_pressed() or button_b.is_pressed():
            if player_1_board[y_coord][x_coord] == 0: # make sure its not a ship
                display.set_pixel(x_coord, y_coord, 0)
            if button_a.is_pressed():
                x_coord = (x_coord + button_a.get_presses()) % 5 # cycles back
            else: # button_b.is_pressed()
                y_coord = (y_coord - button_b.get_presses()) % 5 # likewise
display.clear()

display.scroll("Player 2 Place Ships")
display.scroll("Press A and B together to place ship")

for i in range(2):
    # 2 ships.
    x_coord = 0 # left
    y_coord = 4 # bottom
    while True:
        display.set_pixel(x_coord, y_coord, 9) # show the selected tile
        if button_a.is_pressed() and button_b.is_pressed():
            # place ship. y coordinate accesses the row.
            if player_2_board[y_coord][x_coord] == 0: # just in case
                player_2_board[y_coord][x_coord] = 1
                display.set_pixel(x_coord, y_coord, 9)
                sleep(1000)
                break
            
        elif button_a.is_pressed() or button_b.is_pressed():
            if player_2_board[y_coord][x_coord] == 0: # make sure its not a ship
                display.set_pixel(x_coord, y_coord, 0)
            if button_a.is_pressed():
                x_coord = (x_coord + button_a.get_presses()) % 5 # cycles back
            else: # button_b.is_pressed()
                y_coord = (y_coord - button_b.get_presses()) % 5 # likewise
display.clear()

# and if you found the copy pasting tedious, take note that there is an exec()
# function in python, that 'simply' runs python code as interpreted from strings.
# think of a way to use them! ^_^

display.scroll("Game start!")
display.show(Image.HEART)
sleep(200)
display.clear()

# now, for the fun part!
p1_points = 0
p2_points = 0
while p1_points < 2 and p2_points < 2:
    for i in range(1,3): # i goes from 1 to 2.
        x_coord = 0 # left
        y_coord = 4 # bottom
        while True:
            display.set_pixel(x_coord, y_coord, 9)
            # attack a ship with A and B! use A or B to navigate!
            # note that turns are based on whoever's playing!
            if button_a.is_pressed() and button_b.is_pressed():
                # attack the square! if failed attack, smirk!
                # concatenation at a higher level
                exec("if player_"+str(i)+"_board[y_coord][x_coord] == 0:\n\tdisplay.show(Image.FABULOUS)\n\tsleep(3000)\n\tdisplay.clear()\n" + \
                     "else: \n\tdisplay.scroll('Hit')\n\tplayer_"+str(i)+"_board[y_coord][x_coord] = 0\n\tp"+str(i)+"_points += 1\n\tsleep(1000)\n")
                break

            elif button_a.is_pressed() or button_b.is_pressed():
                display.set_pixel(x_coord, y_coord, 0)
                if button_a.is_pressed():
                    x_coord = (x_coord + button_a.get_presses()) % 5 # cycles back
                else: # button_b.is_pressed()
                    y_coord = (y_coord - button_b.get_presses()) % 5 # likewise


# whew, so now the loop's broke. the game has ended.
if p1_points == 2:
    display.scroll("Player 1 wins!")
else: # player 2 won
    display.scroll("Player 2 wins!")
