let eje_x = 0
let eje_y = 0
basic.forever(function () {
    serial.writeLine("" + (input.acceleration(Dimension.X)))
    input.setAccelerometerRange(AcceleratorRange.TwoG)
    eje_x = Math.map(input.acceleration(Dimension.X), -1023, 1023, 0, 4)
    eje_y = Math.map(input.acceleration(Dimension.Y), -1023, 1023, 0, 4)
    led.toggle(eje_x, eje_y)
    basic.pause(100)
    basic.clearScreen()
})
