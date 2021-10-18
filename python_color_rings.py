import turtle
colors=['orange','red','white','green']
screen=turtle.Screen()
trtl=turtle.Turtle()
trtl.speed(0)
screen.bgcolor('black')
for x in range(500):
	trtl.pencolor(colors[x%4])
	trtl.width(x/4+1)
	trtl.forward(x)
	trtl.left(20)
