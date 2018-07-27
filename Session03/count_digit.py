counting=True
numb=int(input("Enter a number: "))

count=0
while counting:
    numb=numb//10
    count+=1
    if numb==0:
        counting=False
print("Number of digits =",count)