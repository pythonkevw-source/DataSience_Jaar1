import math
''''#zet € om naar $ en andersom

geldeuro = float(input("Euro"))
wisselkoers = 1.15
print("Bedrag in dollar", geldeuro*wisselkoers)
gelddollar = float(input("Dollar"))
print("Bedrag in euro", geldeuro/wisselkoers)


#toon de macht en vierkants wortel van een getal

getal = float(input("getal"))
print(math.sqrt(getal))
print(math.pow(getal,2))

#rond een getal af met 2 cijfers na de komma, gebruik enkel kennis tot nu toe

cijfer = float(input("cijfer"))
#wiskundig trucje:
afronding = int(cijfer * 100)/100
print(afronding)
#hoe we het gaan doen
print(round(cijfer,2))
'''

'''
23.456 int = 23
als ik * 100 doe eerst is het 2345.6
daar een int van is 2345
/100 komt de komma weer'''

#pas oef 1 en oef 2 aan met round
#oef 1 met 2 cijfer sna de komma
#oef 2 met 3 cijfers na de komma
#zet € om naar $ en andersom

geldeuro = float(input("Euro"))
wisselkoers = 1.15
print("Bedrag in dollar", round((geldeuro*wisselkoers),2))
gelddollar = float(input("Dollar"))
print("Bedrag in euro", round((geldeuro/wisselkoers),2))


#toon de macht en vierkants wortel van een getal

getal = float(input("getal"))
print(round(math.sqrt(getal),3))
print(round(math.pow(getal,2),3))

