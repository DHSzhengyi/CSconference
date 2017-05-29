from microbit import *

while True:
    reading = pin0.read_analog() / 204
    if reading > 4.0:
        pos = 4
    elif reading > 3.0:
        pos = 3
    elif reading > 2.0:
        pos = 2
    elif reading > 1.0:
        pos = 1
    else:
        pos = 0
    # note that this can be written as 
    # pos = reading//1 or
    # pos = int(reading)
    
    # set up a clear screen.
    columns = ['0' for i in range(5)] # you can do this for any iterative types. () bracket your value if needed, convert its type if you like, anything's possible!
    columns[pos] = '9' # set the lit up *column* of pixels. Note that you can make use of nested lists/arrays ([[],[],[]] to make rows of the columns ;)
    
    img = ((''.join(columns) + ':')*5)[0:-1] # [-1] accesses the last item, [-2] the second last... [-len(array_name)] is the first.
    # [a:b] selects the (a+1)th item up to the (b-1)th item.
    # 'separator'.join(array) joins the items inside with a separator (between items)
    
    img = Image(img) # type conversion. the micro:bit will only display variables of type 'Image'
    display.show(img)
