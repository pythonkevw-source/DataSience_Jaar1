#VAR = waarde
#LIST = (x-aantal waardes)
        #  0         1         2        3          4            Dit is de index met start vanaf 0
steden = ["Rome", "Parijs", "Londen", "Malaga", "Brussel"]      #Dit is de value
#print(*steden) # het * haalt de waardes uit de []
#lotto_cijfers = [5,10,11,13,14,15,19,23,35,40,50]
print(steden)
"""for stand in range(5):
    print(steden[stand])"""

for stad in steden: #steden gaat nu al zelf een range hebben waardoor dit variabel is
    print(stad)
"""
for cijfer in lotto_cijfers:
    print(cijfer)"""

steden.append("Genk")
for stad in steden:
    print(stad)
steden.insert(1,"Hasselt")
for stad in steden:
    print(stad, end="\t")
#verschil van append en insert => append is op het einde in te voegen, insert kan je kiezen op welke plaats in het array
#list is een train waarbij iedere value een wagon is

#aanpassen van een item
steden[0] = "Milaan"

#CRUD principe = Create, Update, Read, Delete

#verwijderen
#verwijderen op value => alles springt naar voor => als Hasselt meer in de lijst staat => alleen 1ste weg
steden.remove("Hasselt")
#verwijderen op basis van index
steden.pop(3) #=> indien je geen waarde invult is het altijd de laatste waarde
#EXAMEN VRAAG wat is het verschil tussen POP en remove!!!

steden.clear() #lijst is leeg maar nog aanwezig
del steden #lijst is verwijderd
