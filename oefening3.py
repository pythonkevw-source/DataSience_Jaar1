#Voorzie een lijst met 20 random getallen tussen 10 & 200, wat is het grootste en kleinste getal
import random as rnd
lijst = []

for i in range(20):
    getal = rnd.randint(10, 200)
    lijst.append(getal)

print(lijst)
print("het kleinste getal is",min(lijst))
print("het grootste getal is",max(lijst))