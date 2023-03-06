# Imports go at the top
from microbit import *

import music
while True:
    if button_a.was_pressed():
        display.show(Image.DIAMOND)
        music.play(music.BIRTHDAY)
    elif button_b.was_pressed():
        display.show(Image.DUCK)
        music.play(music.BLUES)
