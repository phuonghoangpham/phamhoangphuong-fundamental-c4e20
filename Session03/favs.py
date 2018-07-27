favs=["death note","netflix","teaching"]
print("Your favorite things so far:")
print("* "*20)
for index, fav in enumerate(favs):
    print("{}. {}".format(index+1,fav))
print("* "*20)

pos=int(input("What position do you want to update?"))
update_fav=input("Your replacing favorite: ")
favs[pos-1]=update_fav

print(favs)

