# to design infinity
from turtle import*
# to set background color
bgcolor('black')
#to set design color
color('yellow')
# to set speed of movement
speed(19)
right(45)
for i in range(150):
    circle(28)
    if 7<i<62:
        left(5)
    if 80<i<133:
        right(5)
    if i<80:
        forward(10)
    else:
        forward(5)
