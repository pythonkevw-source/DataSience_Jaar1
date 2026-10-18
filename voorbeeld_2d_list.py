#puntenboek wiskunde, Nederlands, Engels

puntenboek = [
    [9,6,4], #0
    [7,8,6], #1
    [6,8,9]  #2
]

for e,leerling in enumerate(puntenboek):
    print(e,"|",*leerling)