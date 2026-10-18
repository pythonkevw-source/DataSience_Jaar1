woordenboek = {"kat" : "cat", "hond" : "dog", "vis": "fish"}
"""print(*woordenboek.keys()) #=> puur de key alleen
print(woordenboek["kat"])
"""

print(woordenboek.values()) #=> alleen de values

persoon = {"naam" : "jan", "leeftijd": 35, "geslacht": "man", "woonplaats": "genk"}

for values in persoon: #persoon.values()
    print(values)         #geeft standaard de keys

"""#For loop voor zowel keys als values
for items in persoon.items():
    print(items)
#For loop voor zowel keys als values in een dictonairy
for k,v in persoon.items():
    print(k,v)"""

#iets toevoegen in de dictonairy:
persoon["hobby"] = "Voetbal"
persoon["hobby"] = "zaalVoetbal" # => dit gaat de vorige Hobby vervangen, die key kan er niet 2 keer instaan
persoon.update({"job":"IT", "salaris": 4000}) #=> meerdere keys toevoegen , kan ook een aandere dictonairy toevoegen


for k,v in persoon.items():
    print(k,v)

