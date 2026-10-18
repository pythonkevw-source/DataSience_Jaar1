import random as rnd

#Schrijf een programma dat een getal 10 keer vermenigdvuldigt.
"""getal = int(input("Geef het getal"))
a = 0
while a <= 10:
    getal = getal * 10
    a += 1
    if a > 10:
        break
    print(getal, "aantal keer a", a)"""

#Schrijf een programma dat 10 random getallen tussen 1 en 20 geeft.
"""a = 0
while a <= 10:
    getal = rnd.randint(1, 20)
    a += 1
    if a > 10:
        break
    print(getal, "aantal keer a", a)"""

#Schrijf een programma raad het getal tussen 1 en 100. Geef feedback, groter, kleiner, juist geraden. Hou het aantal gokken bij

randomgetal = rnd.randint(1, 100)
geradengetal = int(input("Welk getal denk je?"))
gokjes = 0

while randomgetal != geradengetal:
    gokjes += 1

    if geradengetal < randomgetal:
        print("Het getal is groter")
        geradengetal = int(input("Raad opnieuw"))

    else:
        print("het getal is kleiner")
        geradengetal = int(input("Raad opnieuw"))
        

print("Je hebt het juist geraden! Dit is gelukt in", gokjes, "keer")


