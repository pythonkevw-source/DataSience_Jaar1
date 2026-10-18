jongens = ["Ben","Mark","Piet","Ben"]
jongens2 = ["Bart","Mario","Pieter","Ben"]
meisjes = ["An","Sofie","Marie","An"]
jongens.extend(meisjes)
print(jongens)

jongens = {"Ben","Mark","Piet","Ben"}
meisjes = {"An","Sofie","Marie","An"}
jongens.update(meisjes)
print(jongens)

lijst_getallen = [1,5,3,1,7,2,3,4]
uniek_beschermd = tuple(set(lijst_getallen))
print(uniek_beschermd)



