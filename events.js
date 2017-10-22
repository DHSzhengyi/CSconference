let count: number = 0;
let temp: number = null;

input.onShake(() => {
    count++;
})

input.onButtonPressed(Button.A, () => {
    temp = input.temperature();
    basic.showString(temp + "*C")
    basic.clearScreen();
})

basic.forever(() => {
    if (input.buttonIsPressed(Button.B) && input.buttonIsPressed(Button.A))
        basic.showString(count + " shakes")
})
