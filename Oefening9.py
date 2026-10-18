# Vul een lijst met willekeurige getallen -50 tot 50. Positieve groen, Negatieve rood
#Pas die aan met zelf een gekozen waarde, indien het grote dan groen, anders geel.

import random as rnd
from colorama import Fore, Back, Style

lijst = []

for i in range(15):
        getal = rnd.randint(-50, 50)
        lijst.append(getal)



print(lijst)
for getal in lijst:
        if getal < 0:
                print(getal)
        else:
                print(getal)