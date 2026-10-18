from tabulate import tabulate

koppen = ["naam", "gemeente", "leeftijd"]
personen = [
    ["Jan", "Hasselt", 35],
    ["Piet", "Genk", 28],
    ["Julie", "Genk", 24],
    ["Amber", "As", 30],
    ["Louise", "Lommel", 31]
]

def toon_data_als_tabel():
    tabel = tabulate(personen, headers=koppen, tablefmt="html")

    # schrijf weg naar html-bestand
    with open("personen.html", "w", encoding="utf-8") as bestand:
        bestand.write(f"""
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>Personen</title>
</head>
<body>
    <h1>Overzicht Personen</h1>
    {tabel}
</body>
</html>
""")

    print("HTML-bestand aangemaakt: personen.html")

toon_data_als_tabel()