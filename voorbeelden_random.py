### import lib + mod
import random
#######

#random getal altijd tussen 0 en 1, nu met 2 cijfers na komma
print(round(random.random(),2))
#random getal tussen 0 en 10
print(int(random.random()*11))
#random getal tussen 5 en 15
print(int(random.random()*11+5))
#random tussen 9 en 16
print(int(random.random()*8+9))
#random tussen - 10 en 15
#eerst uw range berkenen deze is nu 25 (van -10 tot 15) en dan het min doorgeven
print(int(random.random()*25-10))
#random 0 tot 30 enkel even getallen (zonder if)
print(int(random.random()*15)*2)

