#hoe een lijst met items wegschrijven naar een txt bestand


lijst = ["An","Jos","Fons","Piet","Toon"]
bestand = open("tekst.txt", "w")
for cijfers in lijst:
    bestand.write(cijfers+"\n")
    