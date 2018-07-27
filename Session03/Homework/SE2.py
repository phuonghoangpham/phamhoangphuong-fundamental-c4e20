flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Phuong and these are my sheep sizes:", flock, end=" ")

max= 0
for i in flock:
    if i > max:
        max=i
print("Now my biggest sheep has size ",max, " let's shear it")

for i in range(len(flock)):
    if flock[i] == max:
        flock[i] = 8

print("After shearing, here is my flock", flock)

for n in range(1,4):
    for j in range(len(flock)):
        flock[j] += 50
    print("Month",n)
    print("One month has passed, now here is my flock", flock)

total_money = sum(flock) *2
print("My flock has size in total: ", sum(flock))
print("I would get", sum(flock), " *2$ = ", total_money, "$")
