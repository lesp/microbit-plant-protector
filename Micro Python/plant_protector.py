from microbit import *
import music
while True:
    soil = pin1.read_analog()
    if soil < 500 and soil > 200:
        display.show(Image.SAD)
        music.play("C4:1")
        sleep(500)
    elif soil < 200:
        display.show(Image.ANGRY)
        music.play("C4:4")
        sleep(500)
    else:
        display.show(Image.HAPPY)