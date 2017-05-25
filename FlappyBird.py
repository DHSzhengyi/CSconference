from microbit import *
import random

display.scroll("Get ready...")

# Game constants - These variables have capitalised names to suggest that they are not supposed to be edited. (They store constants)
DELAY = 20                      # ms between each frame
FRAMES_PER_WALL_SHIFT = 20      # number of frames between each time a wall moves a pixel to the left
FRAMES_PER_NEW_WALL = 100       # number of frames between each new wall
FRAMES_PER_SCORE = 50           # number of frames between score rising by 1

# Global variables - Variable scopes that allow unrestricted access throughout the code. In Python functions, these are accessed by running 'global <variable_name>'
y = 50
speed = 0
score = 0
frame = 0

# Make an image that represents a pipe to dodge
def make_pipe():
    pipe = Image("00003:00003:00003:00003:00003")
    gap = random.randint(0,3)       # random position on the wall
    pipe.set_pixel(4, gap, 0)       # generate a hole in the pipe at that position
    pipe.set_pixel(4, gap+1, 0)     # hole is two dots tall
    return pipe
    
# create first pipe
pipe = make_pipe() # note that while this pipe does CONTAIN the SAME VALUE as the above pipe, it is NOT the SAME VARIABLE.

# Game loop
while True:
    display.show(pipe)
    
    # flap (negative velocity is upward) if button a was pressed
    if button_a.was_pressed():
        speed = -8
        
    # accelerate down to terminal velocity
    speed += 1
    if speed > 2:
        speed = 2
        
    # move bird, but not off the edge
    y += speed
    if y > 99:
        y = 99
    if y < 0:
        y = 0
        
    # draw bird
    bird_y = int(y / 20) # type conversion to integer
    display.set_pixel(1, bird_y, 9)
    
    # check for collision
    if pipe.get_pixel(1, bird_y) != 0:
        display.show(Image.SAD)
        sleep(500)
        display.scroll("Score: " + str(score))
        break
    
    # move wall left
    if(frame % FRAMES_PER_WALL_SHIFT == 0):
        pipe = pipe.shift_left(1)
    
    # create new wall
    if(frame % FRAMES_PER_NEW_WALL == 0):
        i = make_pipe()
        
    # increase score
    if(frame % FRAMES_PER_SCORE == 0):
        score += 1
    
    # wait 20ms
    sleep(DELAY)
    frame += 1

