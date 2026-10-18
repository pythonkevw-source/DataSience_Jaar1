#Voorzie een lijst met personen, Zorg ervoor dat er een persoon toegevoegd of verwijderd kan worden
personen = ["Sarah", "Wouter", "Nancy", "Elise"]
print(personen)
a = 0
while a < 1 :
    personen.append(str(input("geef een naam om toe te voegen")))
    print(personen)
    personen.remove(str(input("geef een naam om toe te verwijderen")))
    print(personen)
