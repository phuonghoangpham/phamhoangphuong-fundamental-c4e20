from random import randint

numb = randint(0,100)

playing = True
count=0

while playing:
    guess=int(input("Guess my number (0-100)?: "))

    if guess>numb:
        print("A little too large :(")
    elif guess<numb:
        print("Too small.")
    else:
        print("Bingo")
        #playing=False
        break
    
    count+=1
    if count==7:
        print("You lose :(")
        playing=False
