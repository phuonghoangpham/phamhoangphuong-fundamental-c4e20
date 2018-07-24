numb=int(input("Please enter a number: "))
p=numb//2
if numb%2==0:
    for a in range(p):
        for i in range(p):
            print(1,end=" ")
            for j in range(1):
                print(0, end=" ")
        print()
        for x in range(p):
            print(0, end=" ")
            for y in range(1):
                print(1,end=" ")
        print()
else:
    for a in range(p):
        for i in range(p):
            print(1,end=" ")
            for j in range(1):
                print(0, end=" ")
        print(1)
        print()
        for n in range(p):
            print(0,end=" ")
            for m in range(1):
                print(1,end=" ")
        print(0)
        print()
    for x in range(p):
        print(1,end=" ")
        for y in range(1):
            print(0,end=" ")
    print(1)
    print()
    