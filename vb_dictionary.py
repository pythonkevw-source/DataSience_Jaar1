woordenboek = {"kat":"cat","hond":"dog","vis":"fish"}
print(woordenboek.values())
print()

persoon = {
           "naam":"jan",
           "leeftijd":35,
           "geslacht":"man",
           "woonplaats":"genk"
           }
#toont zowel de keys als values in een dictionary
#for k,v in persoon.items():
#    print(k,v)

persoon["hobby"] = "voetbal"
persoon.update({"job":"it","salaris":4000})
for k,v in persoon.items():
    print(k,v)

for item in persoon.items():
    print(item)


