import random as rnd

getallen = []
for i in range(100):
      getallen.append(rnd.randint(1,200))
print(getallen)
y = lambda  x:x+5 if x%2==0 else x*2
#y = lambda x:x*2+5

for i in range(len(getallen)):
    getallen[i] = y(getallen[i])

print(getallen)