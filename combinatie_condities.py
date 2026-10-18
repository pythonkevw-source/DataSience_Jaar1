#bij een EN => alles moet TRUE zijn (zien als een maal)
#bij een OF => is het 1 OF meer (zien als een +)
#NOR is een niet


# 3 verschillende getallen a b c welke is het grootste

"""a = 3
b = 2
c = 1

if a > b:
    if a > c:
        print("a is het grootste")
elif b > c:
    if b > a:
        print("b is het grootste")
else:
    print("c is het grootste")"""

# de vorige gaat MAAR is direct veel te groot als je meerdere getallen hebt, daarom gebruiken we een AND
"""a = 3
b = 9
c = 1

if a > b and a > c:
    print("a is het grootste")
elif b > c and  b > a:
    print("b is het grootste")
else:
    print("c is het grootste")"""

"""#or gebruik:
dier = "kat"

if dier == "kat" or dier == "hond" or dier == "goudvis": #telkens specifeeren met dier == anders gaat die altijd hetzelfde geven anders worden er niets meer getest in de OR functie
    print("huisdier")
else:
    print("ander dier")

"""

#or => wel oppassen met dit soort, want je gaat nooit in de else vallen
getal = 15
if getal > 10 or getal < 100
    print("true")
else:
    print("false")