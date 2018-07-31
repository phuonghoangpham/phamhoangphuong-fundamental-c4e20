print("Hi there, this is a superuser gateway")

loop=True
count=0

while loop:
    username=input("Username: ")

    if username=="c4e":
        password=input("Password: ")
        if password == "codethechange":
            print("Welcome,", username)
            break
        else:
            print("Wrong password.")
    else:
        print("User not found.")

    count+=1
    if count==3:
        print("You failed to log in 3 times, go away.")
        loop=False
    
