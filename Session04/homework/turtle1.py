from turtle import *

shape("turtle")
color("blue")
speed(-1)

for i in range(36):
    for i in range(4):
        left(90)
        forward(100)
    left(75)
    for i in range(4):
        left(90)
        forward(100)
mainloop()
