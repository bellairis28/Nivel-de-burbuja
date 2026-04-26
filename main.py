eje_x = 0
eje_y = 0

def on_forever():
    global eje_x, eje_y
    serial.write_line("" + str((input.acceleration(Dimension.X))))
    input.set_accelerometer_range(AcceleratorRange.TWO_G)
    eje_x = Math.map(input.acceleration(Dimension.X), -1023, 1023, 0, 4)
    eje_y = Math.map(input.acceleration(Dimension.Y), -1023, 1023, 0, 4)
    led.toggle(eje_x, eje_y)
    if False:
        basic.clear_screen()
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(500)
basic.forever(on_forever)
