eerste = lambda x,y: x**2 + y +5
print(eerste(5,2))

tweede = lambda x,y:x*x+(2*x*y) + y*y
print(tweede(5,5))

derde = lambda x,y,z: x*x+z*y+x+5
print(derde(1,2,3))

vierde = lambda x,y: (x*2) if x>y else (x/2) #korte if else bij lambda
print(vierde(5,2))

