let item: Image = images
    .createImage(`
    . . . . .
    . . # . .
    # # # # #
    . # # # .
    . # . # .
`)
let count: number = 0
const DT: number = 25
basic.forever(() => {
    item.showImage(count)
    if (input.buttonIsPressed(Button.A)) {
        basic.pause(DT)
        if (count < 5) count++;
    }
    else {
        basic.pause(DT)
        if (count > -5) count--;
    }
})
