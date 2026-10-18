beschermde_data = ("Admin", "1234", "ABCD")
niet_beschermde_data = ["Admin", "1234", "ABCD"]

niet_beschermde_data[0] = "Nieuwe admin"
print(*niet_beschermde_data)
beschermde_data[0]= "nieuwe admin"
print(*beschermde_data)

#hoe verander ik data in een tuple
beschermde_data = list(beschermde_data)
beschermde_data[0] = "dit zou niet mogen"
beschermde_data = tuple(beschermde_data)
print(beschermde_data)


"""for data in beschermde_data:
    print(data)"""

#print(beschermde_data[-1])