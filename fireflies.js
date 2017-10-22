let clock: number = 0;

radio.onDataPacketReceived((packet) => {
    clock += Math.random(2) + 1;
})

basic.forever(() => {
    if (clock > 7) {
        clock = 0;
        radio.sendNumber(0);

        game.addScore(1);

        basic.pause(200);
    } 
    else {
        basic.pause(100);
        clock++;
    }
})

radio.setGroup(12);
radio.setTransmitPower(1);
