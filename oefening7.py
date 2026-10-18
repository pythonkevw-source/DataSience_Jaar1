#Maak een functie kraak de code, hij heeft als feedback, goed, groter, kleiner per getal.

import random as rnd

def code_kraker():
    randomgetal = rnd.randint(1, 1000)
    geradengetal = int(input("Welk getal denk je?"))
    gokjes = 0
    goklijst= []
    goklijst.append(geradengetal)
    while randomgetal != geradengetal:
        gokjes += 1

        if geradengetal < randomgetal:
            print("Het getal is groter")
            geradengetal = int(input("Raad opnieuw"))
            goklijst.append(geradengetal)

        else:
            print("het getal is kleiner")
            geradengetal = int(input("Raad opnieuw"))
            goklijst.append(geradengetal)

    print("Je hebt het juist geraden! Dit is gelukt in", gokjes, "keer")
    print(goklijst)

code_kraker()