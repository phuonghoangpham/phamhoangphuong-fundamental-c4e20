n=int(input("Please enter a number: "))
for i in range(1, n+1):
    #draw 1 line
    s = ''
    for j in range (1,n+1):
        s += '{:2} '.format(i * j)
    print(s)
