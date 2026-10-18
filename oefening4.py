"""Maak een module wiskunde:

Oppv_vierkant, oppv_rechthoek, oppv_cirkel. Inhoud_kubus,
inhoud_balk, inhoud cilinder.

Zorg voor een user interface."""
#########import bib

import math

#############functies
def vierkant():
    zijde = float(input("Geeft de afmeting van een zijde:"))
    opp_vierkant = zijde*zijde
    print("De oppervlakte van uw vierkant is:",opp_vierkant)

def rechthoek():
    lengte = float(input("Geeft de afmeting van een lengte:"))
    breedte = float(input("Geeft de afmeting van een breedte:"))

    opp_rechthoek = lengte * breedte
    print("De oppervlakte van uw rechthoek is:",opp_rechthoek)

def cirkel():
    straal = float(input("Geeft de afmeting van een straal:"))
    opp_cirkel = math.pi*(straal**2)

    print(("De oppervlakte van uw cirkel is:",opp_cirkel))

def kubus():
    zijde = float(input("Geeft de afmeting van een zijde:"))
    opp_kubus = 6 * zijde * zijde
    print("De oppervlakte van uw kubus is:",opp_kubus)

def balk():
    lengte = float(input("Geeft de afmeting van een lengte:"))
    breedte = float(input("Geeft de afmeting van een breedte:"))
    hoogte = float(input("Geeft de afmeting van een hoogte:"))
    opp_balk = 2*(lengte*breedte*hoogte)

    print("De oppervlakte van uw balk is:",opp_balk)

def cilinder():
    diameter = float(input("Geeft de afmeting van een diameter:"))
    hoogte = float(input("Geeft de afmeting van een hoogte:"))
    opp_cilinder = (2*math.pi*(diameter/2))*(hoogte+diameter)

    print("De oppervlakte van uw cilinder is:",opp_cilinder)

def trapezium():
    boven = float(input("Geeft de afmeting van de bovenste lengte:"))
    onder = float(input("Geeft de afmeting van de onderste lengte:"))
    hoogte = float(input("Geeft de afmeting van een hoogte:"))

    opp_trapezium = ((boven + onder)*hoogte)/2

    print(("De oppervlakte van uw trapezium is:",opp_trapezium))

def functies():
    print("1: Bereken oppervlakte van een vierkant")
    print("2: Bereken oppervlakte van een rechthoek")
    print("3: Bereken oppervlakte van een cirkel")
    print("4: Bereken oppervlakte van een kubus")
    print("5: Bereken oppervlakte van een balk")
    print("6: Bereken oppervlakte van een cilinder")
    print("7: Bereken oppervlakte van een trapezium")
    print("stop: stop het programma")


##############################"hoofdprogramma
functies()

keuze=input("Geef een keuzenummer in").lower()
while keuze != "stop".lower():
    if keuze == "1":
        vierkant()
    elif keuze == "2":
        rechthoek()
    elif keuze == "3":
        cirkel()
    elif keuze =="4":
        kubus()
    elif keuze == "5":
        balk()
    elif keuze == "6":
        cilinder()
    elif keuze == "7":
        trapezium()

    functies()
    keuze=input("Geef een keuzenummer in")
