#Voorzie een lijst met 7 willekeurige getallen tussen 15.9 en 75.48, wat is de some van de lijst

import random as rnd
import math
getallijst =[]


for i in range(7):
    getal = round(rnd.uniform(15.9, 75.48), 2)
    getallijst.append(getal)

print(getallijst)
print("som van het array =",sum(getallijst))
