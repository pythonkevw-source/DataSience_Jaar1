#Maak een functie dat het langste woord in een lijst terug geeft.
woorden = ["Pannenkoek", "Aap", "Wortel", "Ananas", "Auto", "Feestdag", "Lessenrooster"]

###### Functies

def tonen():
    print(*woorden)

def toevoegen():
    woord = input("geef een woord om toe te voegen:").capitalize()
    woorden.append(woord)
    print(f"{woord} toegevoegd aan de lijst")

def verwijderen():
    stad = input("geef een woord om te verwijderen:").capitalize()
    woorden.remove((stad))
    print(f"{stad} is verwijders uit de lijst")

def opzoeken():
    stad = input("Geef een woord om op te zoeken").capitalize()
    if stad in woorden:
        print(f"{stad} heb je al bezocht")
    else:
        print(f"{stad} is nog niet bezocht")

def langste_woord():
    longest = max(woorden, key=len)
    print("het grootste woord is", longest)



def functies():
    print("1: toon de woorden")
    print("2: voeg een woord toe")
    print("3: is het woord in de lijst")
    print("4: verwijder een woord uit de lijst")
    print("5: Wat is mijn langste woord")
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
    elif keuze =="5":
        langste_woord()

    functies()
    keuze=input("Geef een keuzenummer in")


