for i in range(0,10):
    #draw 1 line
    for j in range(10):
        if j<=10-i-1:
            print("  ", end="")
        else:
            print("* ", end="")
    print()
