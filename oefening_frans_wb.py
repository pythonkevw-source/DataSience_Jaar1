import random as rnd
woordenboek = {"Hallo":"Bonjour",
               "Geel":"Jaune",
               "Appel":"Pomme",
               "Hond":"Chien",
               "Forrel":"Forrel"}

def toon_woordenboek():
    for nl,fr in woordenboek.items():
        print(nl,fr)

def voeg_woord_toe():
    ned = input("geef het Nederlandse woord")
    fra = input("geef het Franse woord")
    woordenboek[ned]=fra

def zoek_woord():
    zoekwoord = input("geef het woord dat je wenst te zoeken").capitalize()
    if zoekwoord in woordenboek.keys():
        print(f"de vertaling van {zoekwoord} : {woordenboek[zoekwoord]}")
    else:
        print("woord niet gevonden")

def verwijder_woord():
    zoek_woord = input("welk Nederlands woord wil je verwijderen").capitalize()
    if zoek_woord in woordenboek.keys():
        woordenboek.pop(zoek_woord)
        print(f"{zoek_woord} is verwijderd")
    else:
        print("woord niet gevonden")

def pas_vertaling_aan(): #basis key
    zoekwoord = input("geef het nl woord").capitalize()
    if zoekwoord in woordenboek.keys():
        vertaling = input("geef de nieuwe vertaling")
        woordenboek["zoekwoord"] = vertaling
    else:
        print("woord niet gevonden")

def verander_op_basis_value():
    zoekwoord = input("welke franse vertaling wil je veranderen").capitalize()
    for k,v in woordenboek.items():
        if v == zoekwoord:
            woordenboek.pop(k)
            nieuwe_nl = input("wat is de nieuwe nl woord").capitalize()
            nieuwe_fr = input("wat is de Franse vertaling").capitalize()
            woordenboek[nieuwe_nl] = nieuwe_fr
            #zonder pop = woordenboek[k] = nieuwe franse woord



def oefen_woorden():
    for i in range(3):
        woord = rnd.choice(list(woordenboek.keys()))
        print(f"Wat is het Fransewoord voor {woord}")
        vertaling = input("geef het fransewoord").capitalize()
        if vertaling == woordenboek[woord]:
            print("goed")
        else:
            print("fout")

verander_op_basis_value()
toon_woordenboek()


#1 pas vertaling aan
#2 oefen 3 random vragen krijgt.
#3 userinterface while.

