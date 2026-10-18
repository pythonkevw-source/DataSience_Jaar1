"""#WHILE is met een voorwaarde
#FOR is een aantal keer

#Als je meer dan 2 keer iets doet gebruikt dan een loop
#for i = ... (een iterator, tellertje)

getal = 7

for i in range(1,11):
    print(f"{getal} x {i} = {getal * i}")

tekst = "ik zal braaf zijn en naar de leerkracht luisteren"
#schrijf straf 200keer
            #van 1 => 200            van 0 tot 199
for i in range(1,201): #of for i in range(200)
    print(tekst)

aantal = 100
for i in range(aantal):
    print(tekst)

bereik = range(5,105,5) #ik print van 5 tem 104 met intervallen van 5
#van, tot,interval (sprongen van)
for i in bereik:
    print(i)

bereik1 = range( 105,5,-1) #aftellen van 105 tot 6"""


for boven in range(1,11): #rijen aanmaken
    for links in range(1,11): #kolommen aanmaken
        print(boven*links,end="\t") #\t is voor een tab te zetten naar de volgende regel
    print("")  #spatie tussen mijn nummers