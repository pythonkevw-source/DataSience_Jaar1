        # 0     1      2       3
namen = ["An","Ben","Cedrid","Dana"]

def toon_namen():
    for naam in namen:
        print(naam)

def voeg_naam_toe():
    naam = input("geef de naam van de persoon")
    namen.append(naam.capitalize())
    print(f"{naam} toegevoegd aan de lijst")

def bestaat_de_naam():
    naam = input("geef een naam, en kijk of aanwezig in de lijst")
    if naam.capitalize() in namen:
        print(f"{naam} is in de lijst")
    else:
        print(f"{naam} is niet in de lijst")

def verwijder_persoon():
    naam = input("geef de naam van de persoon die je wilt verwijderen").capitalize()
    if naam in namen:
        namen.remove(naam)
        print(f"{naam} is verwijderd uit de lijst")
    else:
        print(f"{naam} niet gevonden")

def verander_naam():
    toon_namen()
    oude_naam = input("geef de naam van de persoon wiens je wilt verander").capitalize()
    if oude_naam in namen:
        nieuwe_naam = input("geef een nieuwe naam").capitalize()
        positie = namen.index(oude_naam)
        namen[positie] = nieuwe_naam
        #namen[namen.index(oude_naam)] = nieuwe_naam 
        print(f"{oude_naam} heeft nu {nieuwe_naam}")
    else:
        print("Naam niet in de lijst.")


def functies():
    print("1: toon de namen")
    print("2: voeg een naam toe")
    print("3: is de naam in de lijst")
    print("4: verwijder een naam uit de lijst")
    print("5: verander naam")
    print("stop: stop het programma")

#######################HOOFDPROGRAMMA######################

functies()
keuze = input("maak je keuze")
while keuze.lower() != "stop":
    if keuze == "1":
        toon_namen()
    elif keuze == "2":
        voeg_naam_toe()
    elif keuze == "3":
        bestaat_de_naam()
    elif keuze == "4":
        verwijder_persoon()
    elif keuze == "5":
        verander_naam()
    elif keuze.lower() == "stop":
        print("tot ziens")
    else:
        print("verkeerde invoer")

    functies()
    keuze = input("maak je keuze")

