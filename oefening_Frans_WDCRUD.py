from multiprocessing.pool import worker

woordenboek = {"Hallo":"Bonjour", "Geel":"Jaune", "Appel": "Pomme", "Hond": "Chien", "Forrel": "Forrel"}

def toon_woordenboed():
    for nl,fr in woordenboek.items():
        print(nl,fr)

def voeg_woord_toe():
    ned = input("Geef het Nederlandse woord")
    fra = input("Geeft het Franse woord")
    woordenboek[ned]=fra
    print(woordenboek)

def zoek_woord():
    zoekwoord = input("geeft het woord dat je wenst te zoeken").capitalize()
    if zoekwoord in woordenboek.keys():
        print(f"de vertaling van {zoekwoord} : {woordenboek[zoekwoord]}")
    else:
        print("Dit woord is niet gevonden")
def verwijder_woord():
    zoekwoord = input("geeft het NL woord dat je wenst te verwijderen").capitalize()
    if zoekwoord in woordenboek.keys():
        woordenboek.pop(zoekwoord)
        print(f"{zoekwoord} is verwijderd")
    else:
        print("Dit woord is niet gevonden")




#1 pas vertaling aan
def vertaling_aanpassen():
    veranderwoord = input("geeft het NL woord dat je wenst te wisselen").capitalize()

    if veranderwoord in woordenboek.keys():
        nieuw_woord = input("geeft het nieuw woord").capitalize()
        woordenboek["veranderwoord"]= nieuw_woord
        print(woordenboek)
    else:
        print("woord niet gevonden")

def verand_op_bais_value():
    zoekwoord = input("Welke franse vertaling wil je veranderen")
    for k,v in woordenboek.items():
        if v== zoekwoord:
            woordenboek.pop(k)
            nieuwe_nl = input("Wat is de nieuwe key")
            nieuwe_fr = input("Wat is de franse vertaling")
            woordenboek[nieuwe_nl]= nieuwe_fr
            #zonder pop = woordenboek[k] = nieuwe_fr



vertaling_aanpassen()
toon_woordenboed()

#2 oefen 3 random vragen krijgt
def oefen_woorden():
    for i in range(3):
        woord = rnd.choice(list(woordenboek.keys()))
        print(f"wat is het franse woord voor {woord}")
        vertaling = input ("geef het franse woord").capitalize()
        if vertaling == woordenboek[woord]:
            print("goed")
        else:
            print("fout)")


#3 userinterface while