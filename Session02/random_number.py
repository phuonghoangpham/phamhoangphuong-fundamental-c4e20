from random import randint

rand_numb = randint (0,100)

if rand_numb<30:
    print("I'm feeling sad")
elif rand_numb<60:
    print("I'm feeling OK")
else: print("I'm feeling great")

print(rand_numb)