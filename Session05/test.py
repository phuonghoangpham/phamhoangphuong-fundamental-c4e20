#quy = ["Quy", 20, "Vinh Phuc", 2, 3, ["Anime", "ping pong"]]
#dictionary 
#CRUD
#key : value
person = {
    "name": "Quy",
    "age": 20,
    "university": "hust",
    "ex": 2,
    "favs": ["anime", "ping pong"]
}

#print(person)

# key = "hometown"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

#print all keys:
#for key in person.keys():
    #print(key, end="\t")

#print all pairs (key, value)
# for key, value in person.items():
#     print(key, value)

#print all values:
# for value in person.values():
#     print(value)

#add one more key, value:
# person["gender"] = "male"
# print(person)

#update one pair (ex 20 instead of 2):
# person["ex"] = 20
# print(person)

#delete one pair:
del person["age"]
print(person)