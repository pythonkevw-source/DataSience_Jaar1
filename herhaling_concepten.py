import random
"""#list []
#index value-principe
#geordende
#aanpasbaar
lotto_cijfers = []
for i in range(7):
    getal = random.randint(1,45)
    lotto_cijfers.append(getal)

#toevoegen = append(1 item)/extend(lijstype)
#verwijderen = pop(index), remove(value)
#index = geeft de eerste index van value(x)

eetdag = ["Pizza","Frieten","Kebab","Pizza","Kebab","Pizza"]
print(eetdag.count("Kebab"))"""

#dictionary {key:value}
#Key-Value #key is uniek.

auto1 = {"merk":"bmw","model":"3-reeks","bouwjaar":2025}
auto2 = {"merk":"bmw","model":"5-reeks","bouwjaar":2025}

wagen_park = {"Mark":auto1,"Dirk":auto2}
for persoon,auto in wagen_park.items():
    print("---------------------")
    print(persoon)
    print("---------------------")
    for kenmerk_k,kenmerk_v in auto.items():
        print(kenmerk_k,":",kenmerk_v)

#toevoegen
#dictionary["key"] = value of dictionary.update()
"""wagen_park["Hans"] = {"merk":"bmw","model":"3-reeks","bouwjaar":2026}
print(wagen_park)
def nieuwe_eigen_wagen():
    naam_eigenaar = input("geef de naam")
    merk = input("wat is het merk")
    model = input("wat is het model")
    bouwjaar = input("wat is het bouwjaar")
    wagen_park[naam_eigenaar] = {"merk":merk,"model":model,"bouwjaar":bouwjaar}

nieuwe_eigen_wagen()
print(wagen_park)
#verwijder = pop(key)
"""

"""#enumerate opsomming van index en values
namen = ["jan","piet","klaas"]
for e, naam in enumerate(namen):
    print(e,naam)"""

#tuples= immutable: niet aanpasbaar ()
#index value
getallen = (5,9,5,2,8)
for e, getal in enumerate(getallen):
    print(e,getal)

