#Maak een functie die 2 lijsten samenvoegd. Deze geeft een lijst terug

lijst1 = [ "Choco", "Pindakaas", "Jam", "Siroop"]
lijst2 = ["boterham", "Croissant", "Pistole", "Sandwich"]

def samenvoegen_lijsten():
    lijst1.extend(lijst2)
    print(lijst1)

samenvoegen_lijsten()