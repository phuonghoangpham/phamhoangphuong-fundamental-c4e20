from turtle import *

shape('turtle')
color('blue')
speed(-1)
side=200
square=0

while square<40:
    side-=3
    square+=1
    for i in range(4):
        left(90)
        forward(side)
    right(10)
        
mainloop()

#chị vẽ ko chuẩn lắm, em sửa hộ chị với nhé 