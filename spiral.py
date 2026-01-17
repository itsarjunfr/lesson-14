import turtle
turtle.Screen().bgcolor('orange')
spiral = turtle.Turtle()
x=1
max=int(input('Size: '))
while x<=max:
    x=x+5
    spiral.forward(x)
    spiral.left(90)
turtle.done()
    