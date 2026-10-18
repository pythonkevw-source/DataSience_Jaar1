"""while True:
    print("hallo")"""

"""a = 2
while a <10:
    a += 1  #a = a + 1
    if a ==5:
        break #indien a 5 is geworden mag je uit de while lus
    print(a)

a = 2
while a <10:
    print("in de loop")
    if a ==5:
        a +=1
        continue 
    print(a)
    a += 1  #a = a + 1
"""

a = 2
b = 1

while a < 10:
    a +=1
    b +=2
    print("outerloop")
    while b < 15:
        if b%2 ==1:
            break
        print("innerloop")
        print("einde")