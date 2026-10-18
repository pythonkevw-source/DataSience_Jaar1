#tuple met 3 lijsten
secret_number= ([0,9,51,85],[9,5,8,6],[7,8,6,1])
secret_number[0].append(15) #inhoud van lijsten kan veranderen omdat dit lijsten zijn in een tuple

#lijsten toevoegen kan niet want dit is een tuple
secret_number= [([0,9,51,85],[9,5,8,6],[7,8,6,1]), [1,2,3]]
for list_items in secret_number:
    print(list_items)

secret_number[0][0].append(1) #dit is 2x [0][0] om in de tuple en dan in de lijst ervan te raken en 1 in de lijst toe te voegen

"""for row in secret_number:
    print(row)"""