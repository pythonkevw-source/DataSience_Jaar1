persoon1 = {"Naam" : "Bart", "Gemeente": "Hasselt", "Auto": {"Merk":"Ford", "Model": "Focus", "Bouwjaar": 1999, "Brandstof": "Benzine"}}
persoon2 = {"Naam" : "An", "Gemeente": "Genk", "Auto": {"Merk":"Tesla", "Model": "ModelY", "Bouwjaar": 2026, "Brandstof": "Elektrisch"}}
persoon3 = {"Naam" : "Jos", "Gemeente": "Bilzen", "Auto": {"Merk":"Opel", "Model": "Corsa", "Bouwjaar": 2004, "Brandstof": "Benzine"}}
persoon4 = {"Naam" : "Caroline", "Gemeente": "Tessenderlo", "Auto": {"Merk":"Skoda", "Model": "Octavia", "Bouwjaar": 2020, "Brandstof": "Diesel"}}
persoon5 = {"Naam" : "Fons", "Gemeente": "Diepenbeek", "Auto": {"Merk":"Mercedes", "Model": "GLA", "Bouwjaar": 2010, "Brandstof": "Diesel"}}

Lijst_personen = [persoon1,persoon2,persoon3,persoon4, persoon5]

#print(Lijst_personen)
def toon_naam_nummer():
    for e,persoon in enumerate(Lijst_personen):
        print(e,persoon["Naam"])

def toon_info():
    for e, info in enumerate(Lijst_personen):
        print(f"lijstnummer {e}")
        print(f"Naam: {info["Naam"]}")
        print(f"Gemeente: {info["Gemeente"]}")
        print("---Auto info---")
        for auto_key, auto_value in info["Auto"].items():
            print(auto_key,":",auto_value)
        print("")
        print("#################")
    print(f"aantal personen {len(Lijst_personen)}")

def voeg_persoon_toe():
    naam = input("Geeft de naam:")
    gemeente = input("Geef de Gemeente:")
    auto = {}
    Lijst_personen.append({"Naam": naam, "Gemeente": gemeente, "Auto":auto})
    toon_info()

def voeg_auto_toe():
    toon_naam_nummer()
    nummer = int(input("Geef de nummer voor wie je een auto wilt toevoegen:"))
    if nummer > len(Lijst_personen):
        print("ongeldig nummer")
    else:
        merk = str(input("Geeft het merk:"))
        model = str(input("geeft het model:"))
        bouwjaar = int(input("Geeft het bouwjaar:"))
        brandstof = str(input("Geeft het type brandstof:"))
        Lijst_personen[nummer]["Auto"].update({"Merk":merk, "Model": model, "Bouwjaar": bouwjaar, "Brandstof": brandstof})
    toon_info()

def verwijder_persoon():
    toon_naam_nummer()
    nummer = int(input("Geef de nummer voor wie je wilt verwijderen:"))
    Lijst_personen.pop(nummer)
    toon_info()

def verwijder_auto():
   toon_info()
   toon_naam_nummer()
   nummer = int(input("Geef de nummer voor wie je een auto verwijderen:"))
   if nummer > len(Lijst_personen):
       print("ongeldig nummer")
   else:
       Lijst_personen[nummer]["Auto"].clear()
       toon_info()


"""persoon1 = {"Naam" : "Bart", "Gemeente": "Hasselt", "Auto": {"Merk":"Ford", "Model": "Focus", "Bouwjaar": 1999, "Brandstof": "Benzine"}}
persoon2 = {"Naam" : "An", "Gemeente": "Genk", "Auto": {"Merk":"Tesla", "Model": "ModelY", "Bouwjaar": 2026, "Brandstof": "Elektrisch"}}
persoon3 = {"Naam" : "Jos", "Gemeente": "Bilzen", "Auto": {"Merk":"Opel", "Model": "Corsa", "Bouwjaar": 2004, "Brandstof": "Benzine"}}
persoon4 = {"Naam" : "Caroline", "Gemeente": "Tessenderlo", "Auto": {"Merk":"Skoda", "Model": "Octavia", "Bouwjaar": 2020, "Brandstof": "Diesel"}}

Lijst_personen = [persoon1,persoon2,persoon3,persoon4]
#Met een eerste For loop open ik mijn lijst "Lijst_personen" en pak ik de personen virtueel uit:
    - persoon1 = {"Naam" : "Bart", "Gemeente": "Hasselt", "Auto": {"Merk":"Ford", "Model": "Focus", "Bouwjaar": 1999, "Brandstof": "Benzine"}}
    - persoon2 = {"Naam" : "An", "Gemeente": "Genk", "Auto": {"Merk":"Tesla", "Model": "ModelY", "Bouwjaar": 2026, "Brandstof": "Elektrisch"}}
    - persoon3 = {"Naam" : "Jos", "Gemeente": "Bilzen", "Auto": {"Merk":"Opel", "Model": "Corsa", "Bouwjaar": 2004, "Brandstof": "Benzine"}}
    - persoon4 = {"Naam" : "Caroline", "Gemeente": "Tessenderlo", "Auto": {"Merk":"Skoda", "Model": "Octavia", "Bouwjaar": 2020, "Brandstof": "Diesel"}}
#Met de 2de For loop open ik mijn dictionary bvb :"Persoon1" en heb ik een KEY + VALUE waarde
    -  KEY   : VALUE
    - "Naam" : "Bart", 
    - "Gemeente": "Hasselt", 
    - "Auto": {"Merk":"Ford", "Model": "Focus", "Bouwjaar": 1999, "Brandstof": "Benzine"}
#Met de 3de FOR met de VALUE van For2 pak ik virtueel de volgende dictionary uit
    - "Merk":"Ford", 
    - "Model": "Focus", 
    - "Bouwjaar": 1999, 
    - "Brandstof": "Benzine"
#Met een 4de For moet ik de value hebben met de index 1 van FOR3, en deze in een set() steken.
    - set("Ford")
"""

def unieke_auto():
    uniek_lijst = []
    for items in Lijst_personen:
        #print(items)                                       # items is van het type dict
        for persoon_key,persoon_value in items.items():
           #print(persoon_key, end='\t')
           #print(persoon_value)
            if persoon_key == "Auto":
                 for uniek_key, uniek_value in persoon_value.items():
                     #print(uniek_key, end='\t')
                     #print(uniek_value)
                     if uniek_key == "Merk":
                        #print(uniek_value)
                        uniek_lijst.append(uniek_value)
                        uniek_set = set(uniek_lijst)

    print(uniek_set)


    """unieke_merken = set()

    for items in Lijst_personen:
        if "Auto" in items:
            auto = items["Auto"]
            if "Merk" in auto:
                unieke_merken.add(auto["Merk"])
    print(unieke_merken)"""





    #############"hoofdprogramma###################
#toon_info()
#voeg_persoon_toe()
#voeg_auto_toe()
#verwijder_persoon()
#verwijder_auto()
unieke_auto()