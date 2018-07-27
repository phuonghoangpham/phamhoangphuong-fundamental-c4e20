fav=["death note", "netflix", "teaching"]
print("Hi there, here's your favorite things so far: ", *fav, sep=", ")

new_fav=input("Name one thing you want to add:")
fav.append(new_fav)
print("Name one thing you want to add:", *new_fav)