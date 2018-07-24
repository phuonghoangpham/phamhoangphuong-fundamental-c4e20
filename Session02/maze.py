from turtle import *

shape('turtle')
color('green')
speed(-1)
length=5

for i in range(0,800, 10):
    forward(length)
    left(90)

    length=length+5 #length+=5

mainloop()