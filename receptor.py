from microbit import *
# Importamos radio
import radio

'''
   Configuración Radio
'''   
radio.on()
radio.config(channel=3)

while True:
    message=radio.receive()
    sleep(20)
    if message is not None:
        display.scroll(str(message))
