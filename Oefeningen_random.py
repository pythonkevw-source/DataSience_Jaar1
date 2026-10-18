import random as rnd

#Schrijf een programma dat 3 random getallen optelt.
print((rnd.random() + rnd.random() + rnd.random()))

#Schrijf een programma dat een random getal genereert tussen 25 en 50
print(rnd.randint(25,50))
#Schrijf een programma dat een random getal geneert tussen 13.7 en 19.8 met 2 dec na de komma
print(round(rnd.uniform(13.7, 19.8),2))
#Schrijf een programma dat 2 getallen geneert a en b tussen 0 en 6 : a is groter, b is groter of a en b zijn even groot
getala = (rnd.randint(0,6))
getalb = (rnd.randint(0,6))

if getala > getalb:
    print("a is", getala, "en groter")
elif getala < getalb:
    print("b is", getalb, "en groter")
else:
    print("a", getala, "& b", getalb, "zijn even groot")