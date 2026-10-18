#Test of een string een palandroom is. Lepel, kaak, racecar

tekst = str(input("Geef mij het woord om te checken als het een palandroom is"))

if tekst == tekst[::-1]:  # van begin naar het eind, met stappen achteruit
    print("Dit is inderdaad een palandroom!")
else:
    print("Dit is geen palandroom :(")