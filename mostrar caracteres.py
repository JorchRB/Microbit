# Imports go at the top
from microbit import *

texto = "Microbita"
i=0
while(i<len(texto)):
    display.show(texto[i])
    i = i + 2
    sleep(500)
