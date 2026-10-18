myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

myfamily["child4"] = {"name":"Jef","year":2016}
for k_family, v_family in myfamily.items():
    for k_child, v_child in v_family.items():
        print(k_child,v_child)

