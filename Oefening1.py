#Maak lijst met bezochte plaatsen, zorg dat je plaats kan toevoegen, verwijderen, en opzoeken(bezocht, niet bezocht)

plaatsen = ["Genk", "Londen", "Malaga", "Parijs", "Hasselt", "Bologna", "Sevilla"]

###### Functies

def tonen():
    print(*plaatsen)

def toevoegen():
    stad = input("geef de naam van de plaats om toe te voegen:").capitalize()
    plaatsen.append(stad)
    print(f"{stad} toegevoegd aan de lijst")

def verwijderen():
    stad = input("geef de naam van de plaats om te verwijderen:").capitalize()
    plaatsen.remove((stad))
    print(f"{stad} is verwijders uit de lijst")

def opzoeken():
    stad = input("Geef de naam van de plaats om op te zoeken").capitalize()
    if stad in plaatsen:
        print(f"{stad} heb je al bezocht")
    else:
        print(f"{stad} is nog niet bezocht")

def functies():
    print("1: toon de plaatsen")
    print("2: voeg een plaats toe")
    print("3: is de plaats in de lijst")
    print("4: verwijder een naam uit de lijst")
    print("stop: stop het programma")

#########Hoofdprogramma
functies()

keuze=input("Geef een keuzenummer in").lower()
while keuze != "stop".lower():
    if keuze == "1":
        tonen()
    elif keuze == "2":
        toevoegen()
    elif keuze == "3":
        opzoeken()
    elif keuze =="4":
        verwijderen()

    functies()
    keuze=input("Geef een keuzenummer in")
