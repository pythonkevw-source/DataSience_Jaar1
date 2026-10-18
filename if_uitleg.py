#if met 2 opties (waar / nietwaar)
'''getal = 7
#print(getal == 5)

# = teken toekennen A = 5
# == waarde vergelijken (true of false waarde)

if getal == 5:
    print("getal is 5")
else:
    print("getal is niet een 5")

#getal 5, groter of kleiner
getal = 6
if getal == 5:
    print("getal is 5")
elif getal < 5:
    print("getal is < dan 5")
else:
    print ("getal is > dan 5")'''

'''#is mijn getal kleiner dan 100, <10 of groter dan 100
getal = 5

if getal < 10:
    print("getal < 10")
elif getal < 100:
    print("getal < 100")
else:
    print("getal is 100 of groter")'''

#is mijn getal kleiner dan 100, <10 of groter dan 1000 met alleen if
#dit gaat het aantal if geven dat waar is => dus bij 1111 gaan het de 3 if's worden
getal = 110
if getal < 10:
    print("kleiner dan 10")
if getal >10:
    print("groter dan 10")
if getal > 100:
    print("groter dan 100")
if getal > 1000:
    print("groter dan 1000")



getall = 5
if getall != 5:
    print("getal is niet 5")
else:
    print("getal is 5")

#1 regel if en 1 lijn else
getal = 8
if getal ==5: print("getal is 5")
print("getal is 5") if getal ==5 else print("getal is niet 5")

#oefening: <3jaar baby, <10j kind <18jaar tiener, 18+ volwassen

leeftijd = int(input("geef je leeftijd"))
if leeftijd < 3:
    print("baby")
elif leeftijd < 10:
    print("kind")
elif leeftijd < 18:
    print("tiener")
else:
    print("volwassen")
