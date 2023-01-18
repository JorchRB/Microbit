from microbit import *
n=1
cuadrao1 = Image("00000:56789:56789:56789:00000")
cuadrao2 = Image("00000:56789:56789:56789:00000")
cuadrao3 = Image("00000:56789:56789:56789:00000")
cuadrao4 = Image("00000:56789:56789:56789:00000")
cuadrao5 = Image("00000:56789:56789:56789:00000")
while n <= 10:
    if n %2 == 0:
        display.show(cuadrao1)
    else:
        display.show(cuadrao2)
    sleep(500)
display.scroll("FIN")
