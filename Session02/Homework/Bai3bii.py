n=int(input("Enter the total numbers of 1's and 0's: "))
p=n//2
if n%2==0:
    for i in range(p):
        print(1, end=" ")
        for j in range(1):
            print(0, end=" ")
if n%2==1:
    for i in range(p):
        print(1, end=" ")
        for j in range(1):
            print(0, end=" ")
    print(1)
