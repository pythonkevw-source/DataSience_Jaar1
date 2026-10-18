from tabulate import tabulate

koppen = ["naam","gemeente","leeftijd"]
personen = [
    ["Jan","Hasselt",35],
    ["Piet","Genk",28],
    ["Julie","Genk",24],
    ["Amber","As",30],
    ["Louise","Lommel",31]
]

#toon index en data
def toon_data():
    print("index, naam, gemeente, leeftijd")
    for e,persoon in enumerate(personen):
        print(e,*persoon)

#voeg een persoon toe. Persoon = list toevoegen.
def voeg_persoon_toe():
    naam = input("geef de naam").capitalize()
    gemeente = input("geef de gemeente").capitalize()
    leeftijd = int(input("geef de leeftijd"))
    persoon = [naam,gemeente,leeftijd]
    personen.append(persoon)

#toon namen
def toon_namen():
    for naam in personen:
        print(naam[0])

def geef_namen():
    res = []
    for naam in personen:
        res.append(naam[0])
    return res

#komt naam voor in de lijst
def zoek_naam_persoon():
    zoek_naam = input("geef de naam die je zoekt")
    if zoek_naam in geef_namen():
        print("gevonden")
    else:
        print("niet gevonden")

#verwijder_persoon
def verwijder_persoon():
    toon_data()
    nummer = int(input("geef het nummer dat je wilt verwijderen"))
    if nummer < len(personen):
        personen.pop(nummer)
        print(f"persoon is verwijderd")
    else:
        print("ongeldig nummer")

#toon_data in een tabel.
def toon_data_als_tabel():
    tabel = tabulate(personen,headers=koppen,tablefmt="html")
    print(tabel)


toon_data_als_tabel()
print("")