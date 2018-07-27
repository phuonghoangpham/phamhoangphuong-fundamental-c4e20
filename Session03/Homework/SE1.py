choosing = True
items = ["T-Shirt", "Sweater"]

while choosing:
    option = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if option == "R" or option =="r":
        print("Our items: ", end ="")
        print(*items, sep=", ")
    elif option == "C" or option =="c":
        new_option = input("Enter new item: ")
        items.append(new_option)
        print("Our items: ", end ="")
        print(*items, sep=", ")
    elif option == "U" or option =="u":
        update_position = int(input("Update position? "))
        updated = input("New item? ")
        items[update_position - 1] = updated
        if updated-1>len(items) or updated-1<0:
            print("Index out of range.")
        else:
            print("Our items: ", end ="")
            print(*items, sep=", ")
    elif option == "D" or option == "d":
        del_option = int(input("Delete position? "))
        del items[del_option - 1]
        print("Our items: ", end ="")
        print(*items, sep=", ")
    
    