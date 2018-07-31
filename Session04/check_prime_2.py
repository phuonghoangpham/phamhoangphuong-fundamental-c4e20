numb=int(input("Enter a number: "))

is_prime=True

loop=True
i=2

while i<numb**2:
    if numb%i==0:
        is_prime=False
    i+=1
    if i==numb:
        loop=False

if is_prime==True:
    print("{} is a prime number".format(numb))
else:
    print("{} is not a prime number".format(numb))