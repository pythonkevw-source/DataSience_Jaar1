#Simuleer een kop of munt: vraag naar aantal keer, steek alle waarde in een lijst, geef daarna % kop en % munt.
import random as rnd
aantal_gokjes = []


aantal_worpen = int(input("hoeveel keer wil je gooien?"))

for gokjes in range(aantal_worpen):
    kop_munt = rnd.randint(0, 1)

    if kop_munt == 0:
        coin = "kop"
        aantal_gokjes.append("Kop")
    else:
        coin = "munt"
        aantal_gokjes.append("Munt")

kop_gokjes = aantal_gokjes.count("Kop")
print(f"aantal keer kop: {kop_gokjes}, dit is {(kop_gokjes/aantal_worpen)*100}%" )
munt_gokjes = aantal_gokjes.count("Munt")
print(f"aantal keer kop: {munt_gokjes}, dit is {(munt_gokjes/aantal_worpen)*100}%" )
