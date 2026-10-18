#list van dictionaries, die een list bevat

persoon1 = {"Naam":"Geert","Leeftijd":50,"Hobbies":["Voetbal","Wielrennen","Sportkrant lezen"]}
persoon2 = {"Naam":"Gert","Leeftijd":45,"Hobbies":["Voetbal","Reizen"]}
persoon3 = {"Naam":"Valerie","Leeftijd":30,"Hobbies":["Lezen","Reizen","Paarden"]}
persoon4 = {"Naam":"Peter","Leeftijd":16,"Hobbies":["Gamen"]}
lijst_personen = [persoon1,persoon2,persoon3,persoon4]

def toon_info():
    for e,persoon in enumerate(lijst_personen):
        print(f"lijstnummer {e}")
        print(f"naam :{persoon["Naam"]}")
        print(f"leeftijd : {persoon["Leeftijd"]}")
        print("--hobbies--")
        for hobby in persoon["Hobbies"]:
            print(hobby,end="\t")
        print("")
        print(" --- ")
    print(f"aantal personen {len(lijst_personen)}")

def toon_naam_nummer():
    for e,persoon in enumerate(lijst_personen):
        print(e,persoon["Naam"])

def voeg_persoon_toe():
    naam = input("geef naam van de persoon")
    leeftijd = int(input("leef de leeftijd in"))
    hobbies = [] #een lege lijst, want bij het aanmaken nog geen gekende hobbies
    lijst_personen.append({"Naam":naam,"Leeftijd":leeftijd,"Hobbies":hobbies})

def voeg_hobby_toe_aan_persoon():
    #wie en wat

    toon_naam_nummer()
    nummer = int(input("welke nummer wil aanspreken")) #wie
    if nummer > len(lijst_personen):
        print("ongeldig numemr")
    else:
        hobby = input("geef de hobbie van de persoon")
        lijst_personen[nummer]["Hobbies"].append(hobby)

def verwijderen_een_persoon():
    #wie moet eruit, index
    toon_naam_nummer()
    nummer = int(input("geef het nummer van de persoon die je wenst te verwijderen"))
    if nummer < len(lijst_personen):
        lijst_personen.pop(nummer)
    else:
        print("ongeldige nummer")

#voeg_hobby_toe_aan_persoon()
#verwijderen_een_persoon()
toon_info()
