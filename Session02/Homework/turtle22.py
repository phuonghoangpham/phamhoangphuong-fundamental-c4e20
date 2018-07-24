
from turtle import *

speed (-1)
shape("classic")

for i in range (3, 7):
    angle = 360/i
    if i % 2 == 1:
        color("blue")
        for j in range(i):
            forward(100)
            left(angle)
                    
    else:
        color("red")
        for n in range(i):
            forward(100)
            left(angle)
        
exitonclick()
mainloop()