print("Hi there, this is a superuser gateway")

username = input("Username: ")
if username != "c4e":
    print("You are not a super user.")
else:
    import getpass
    password = getpass.getpass('Password:')
    if password!= "codethechange":
        print("Incorrect password")
    else:
        print("Welcome", username)