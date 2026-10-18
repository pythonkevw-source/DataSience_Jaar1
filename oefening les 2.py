import math
"""    #oefening 1: Maak een deelprogramma dat de deling en de rest terug geeft 19/3 = 6 rest 1
Getal = 19
print("getal is", int(Getal/3) , "rest is" ,19%3)

    #oefening 2: Schrijf een programma dat de omtrek van een cirkel berekent
r = float(input("Geef de r"))
print("omtrek van de cirkel is", (2 * r * math.pi) )

    #oefening 3: Schrijf een programma dat de oppervlakte van een kubus berekent

sa = float(input("geeft de zijde"))
print("oppervlakte van de kubus is", (6*(sa**2)), "m²")

    # oefening 4: Schrijf een programma dat de inhoud van een balk berekent dat voor x procent gevuld is
l =  float(input("geeft de lengte"))
b = float(input("geeft de breedte"))
h = float(input("geeft de hoogte"))
percent = float(input("geeft aan hoeveel % gevuld"))
print("Inhoud van de balk is:", (l*b*h)/(percent/100), "m³")

    #oefening 5: Schrijf een programma dat graden °c omzet naar °f
graden = float(input("hoeveel graden is het nu?"))
print("Het is nu", graden,"C°, dit komt overeen met:", (graden*1.8)+32,"F°")

    #oefening 6: Schrijf een programma dat het aantal graden van een n hoek berekent = (n-2)*180
aantal_hoeken = int(input("geef het aantal hoeken groter dan 3"))

if aantal_hoeken > 3:
    print("aantal graden per hoek is", (aantal_hoeken-2)*180)
else:
    print("aantal hoeken is kleiner dan 3")
"""

"""#oefening 7: Controleer of een getal deelbaar is door 7
getal = float(input("wat is het getal om te zien als het deelbaar is door 7"))

if getal%7 ==0:
    print("getal is deelbaar door 7")
else:
    print("getal is niet deelbaar door 7")"""

"""
#oefening 8: Geef 2 getallen in. Het programma zegt getal a is groter dan, kleiner dan, even groot.
getal1 = float(input("geeft getal 1"))
getal2 = float(input("geeft getal 2"))

if getal1 > getal2:
    print("getal1",getal1, "is groter dan getal2", getal2)
elif getal1 < getal2:
    print("getal1",getal1, "is kleiner dan getal2", getal2)
else:
    print("de getallen zijn even groot")
"""

"""#oefening 9: Geef een getal in: indien het even is doe het getal maal 2 anders delen door 2
getal = float(input("geef een getal in"))

if getal%2 == 0:
    print("getal is even ik doe het x2:", getal*2)
else:
    print("getal is oneven ik doe het /2", getal/2)"""

"""#oefening 10: Schrijf een programma dat weergeeft welk soort hoek, stomp, recht of scherp
hoek = float(input("Geeft de hoek in:"))

if hoek < 90:
    print("Dit is een scherpe hoek")
elif hoek ==90:
    print("Dit is een rechte hoek")
else:
    print("dit is een stompe hoek")"""

#gevorderde oef
"""#oefening 1: Schrijf een programma dat (a+b)² kan uitrekenen (a² + 2ab + b²)
a = float(input("geef mij a:"))
b = float(input("geef mij b:"))

print(a**2 +2*a*b + b**2)"""

"""#oefening 2: Schrijf een programma dat de schuine zijde van een rechthoek berekent. Pythogras
zijde1 = float(input("zijde1"))
zijde2 = float(input("zijde2"))

print("de schijne zijde is:", math.sqrt(zijde1**2 + zijde2**2))"""

"""#oefening 3: Schrijf een programma dat de oppervlakte van een vijfhoek berekent
s = float(input("geef de lengte van een zijde"))
print("oppervlakte van de vijfhoek is:", (5*s**2)/(4*math.tan(math.radians(36))))"""

"""#oefening 4: Schrijf een programma dat berekent hoeveel 1cm² pizza kost(diameter, prijs)
prijs = float(input("Prijs van de pizza"))
diameter = float(input("diameter van de pizza in cm"))
print("de pizza kost", prijs/(math.pi*(diameter/2)**2), "€ per 1cm²")
"""
"""#oefening 5: Schrijf een programma dat eenheden, tientallen en hondertallen,duizentallen scheidt 1123= 1d,1h, 2t, 3e
getal = int(input("geeft je getal"))

duizentallen = int(getal /1000)
honderdtallen = int((getal/100)%10)
tientallen = int((getal/10)%10)
eenheden = int(getal % 10)

print(f"Jouw getal {getal} heeft {duizentallen}d, {honderdtallen}h, {tientallen}t, {eenheden}e")"""


"""#oefening 6: Schrijf een programma dat volgende boodschap geeft <0(negatief) <10 <100 <1000 <10000
getal = int(input("geeft je getal"))

if getal < 0:
    print("<0>")
elif getal < 10:
    print("<10")
elif getal < 100:
    print("<100")
elif getal < 1000:
    print("<1000")
elif getal < 10000:
    print("<10000")
else:
    print("")"""
