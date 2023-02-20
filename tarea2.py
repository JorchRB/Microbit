# Imports go at the top
from microbit import *

lista_de_animales = ["perro", "gato", "conejo", "cucaracha"]

for i in lista_de_animales:
    display.show(i)
    sleep(1000)
