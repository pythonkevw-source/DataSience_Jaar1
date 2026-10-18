### import lib + mod
import math
############

keuze = int(input("geef keuze"))

if keuze ==1:
    getal = float(input("Geef het getal"))

    if getal % 5 == 0:
        print("getal gedeeld door 5:", getal / 5)
    else:
        print("getal maal 2", getal * 2)
elif keuze == 2:
    getal = float(input("Geef het getal"))
    machtgetal = getal ** 4
                #of math.pow(getal,4)
    if machtgetal % 2 == 0:
        print("getal is", machtgetal, "dit is even")
    else:
        print(f"getal is {machtgetal} oneven")
elif keuze ==3:
    getal1 = float(input("Geef het getal1"))
    getal2 = float(input("Geef het getal2"))
    getal3 = float(input("Geef het getal3"))

    if (getal1 + getal2 + getal3) < 10:
        print("klein getal")
    elif (getal1 + getal2 + getal3) < 100:
        print("gemiddeld")
    else:
        print("groot")
else:
    print("verkeerd")


"""getal = 10
if getal > 10:
    print("groter")
elif getal < 10:
    (print("kleiner"))
else:
    print("gelijk")
    if getal % 2 == 0:
        print("even")
    else:
        print("oneven")"""


"""#Als een getal deelbaar is door 5. delen door 5 anders het getal maal 2
getal = float(input("Geef het getal"))

if getal%5 == 0:
    print("getal gedeeld door 5:", getal/5)
else:
    print("getal maar 2", getal*2)"""

"""#Schrijf een programma dat de 4 macht van een ingegeven getal geeft. Is het deelbaar door 2 even, anders oneven.
getal = float(input("Geef het getal"))
machtgetal = getal**4

if machtgetal%2 ==0:
    print("getal is", machtgetal,"dit is even")
else:
    print("getal is", machtgetal,"oneven")
"""
"""#Schrijf een programma dat 3 getallen optelt. Is de som kleiner dan 10:print("klein getal"),  tussen 10 en 100 ("gemiddeld), anders groot
getal1 = float(input("Geef het getal1"))
getal2 = float(input("Geef het getal2"))
getal3 = float(input("Geef het getal3"))

optelling = (getal1 + getal2 + getal3)

if optelling < 10:
    print("klein getal")
elif optelling > 100:
    print("groot getal")
else:
    print("gemiddeld")"""