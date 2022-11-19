basic.show_icon(IconNames.LEFT_TRIANGLE)
basic.pause(5000)

def on_forever():
    basic.show_string("Salvatore")
    basic.pause(1000)
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(1000)
basic.forever(on_forever)
