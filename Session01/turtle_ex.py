n = int(input("how many sides?"))
angle = 360/n

from turtle import *

speed(-1)
shape("turtle")
color("green")

for i in range(n):
    forward(100)
    left(angle)

mainloop()