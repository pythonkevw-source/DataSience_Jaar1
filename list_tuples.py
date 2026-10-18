#tuple met 3 lijsten.
secret_number = ([0,9,51,85],[9,5,8,6],[7,8,6,1])

secret_number = [([0,9,51,85],[9,5,8,6],[7,8,6,1]) ,[1,2,3] ]
secret_number[0][0].append(15) #inhoud van lijsten kan veranderen
for list_item in secret_number:
    print(type(list_item))

secret_number[0][0].append(1)
print(secret_number[0])


