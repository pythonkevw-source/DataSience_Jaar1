#import random
#je kan ook een import doen en een alias geven aan de import
import random as wil
#snel een alias aanpassen in het gehele document => shift + F6
#snel een lijn boven/onder => lijn selectie => alt + shift + pijltjes

laagste = int(input("geeft laagste in"))
hoogste = int(input("geeft hoogste in"))

#indien gebruiker eerst een klein getal ingeeft en dan een groot
if laagste < hoogste:
    print(wil.randint(laagste, hoogste))
#indien de gebruiker eerst een groot getal ingeeft en dan een klein
else:
    print(wil.randint(hoogste, laagste))
