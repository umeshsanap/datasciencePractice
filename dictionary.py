#declaration

# print(std["name"])
# std["rollno"] = 60
# print(std)

# std[5] = 100
# print(std)

# print(len(std))
# print(type(std))
# RollNoName = ((3,"Radhika"),(2,"Akshada"),(1, "Sakshi"),(4, "Nikita"))
# RollNoName = [1,2,3,4,5]
# RollNoName[1] = "Sakshi"
# print(RollNoName)
# dictConversion = dict(RollNoName)
# print(dictConversion)
# print(std.get("name"))
# print(std.keys())
# print(std.values())
# print(std.items())

std = {
    "name" : "sakshi",
    "friend": "akshada",
    "address" :"Niphad, Nashik",
    "rollno": 23,
    5 : "ABCD",
}
print(f"Old dictionary :- {std}")
copyStd = dict(std)
std.popitem()
std.popitem()
print(f"Old dictionary :- {std}")
print(f"New Dictionary {copyStd}")