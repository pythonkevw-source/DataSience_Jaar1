#Maak een programma dat rekenen sommen willekeurig genereerd.
#Sla de juist en foute op in 2 lijsten, juist of fout. Geef na een fout het juiste antwoord
import random as random

lijst_juist = []
lijst_fout = []

def speel_spel():
    getal1 = random.randint(0, 10)
    getal2 = random.randint(0, 10)
    rekensom = getal1 + getal2
    print(f"wat is de rekensom van {getal1} + {getal2}")
    antwoord = int(input("Wat is jou antwoord?:"))

    if antwoord == int(rekensom):
        lijst_juist.append(rekensom)
        print("Het antwoord is juist!")
        print("Juiste antwoorden:", *lijst_juist)
        print("Je hebt nu", len(lijst_juist), "juiste antwoorden en", len(lijst_fout),"foute antwoorden")
    else:
        lijst_fout.append((antwoord))
        print("foute antwoorden", *lijst_fout)
        print("Uw antwoord is niet juist, het juiste antwoord is", rekensom)

def functies():
     print("1: Geef een antwoord:")
     print("2: stop")


############hoofdprogramma#############
functies()

keuze=input("Geef een keuzenummer in").lower()
while keuze != "stop".lower():
    if keuze == "1":
        speel_spel()
    elif keuze == "2":
        break


