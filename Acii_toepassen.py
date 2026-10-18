tekst = "dit is een tekst omgezet naar ascii"

ascii_lijst = []
versleutel_lijst = []
for letter in tekst:
    ascii_lijst.append(ord(letter))

print(*ascii_lijst)

for nummer in ascii_lijst:
        print(chr(nummer), end="")
        versleutel = nummer + 2
        versleutel_lijst.append((chr(versleutel)))
        print(versleutel_lijst, end="")

print((""))