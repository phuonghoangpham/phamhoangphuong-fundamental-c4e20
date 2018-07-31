print("Guess your number game")
print("Now think of a number from 0 to 100, then press 'Enter' ")
input()

print("""
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' is my guess is 'L'arger than your number
""")

low=0
high=100

playing=True

while playing:
    mid=(low+high)//2
    guess=input("Is {} your number: ".format(mid))

    if guess=='c':
        print("I knew it")
        playing=False
    elif guess=='l':
        low=mid
    elif guess=='s':
        high=mid