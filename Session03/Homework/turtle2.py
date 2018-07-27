from turtle import *

shape("turtle")
colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range(len(colors)):
    begin_fill()
    color(colors[i])
    for a in range(4):
        forward(50)
        left(90)
    end_fill()
    forward(50)

mainloop()