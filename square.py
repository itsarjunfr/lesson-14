colorbg = input('Enter background color: ')
import turtle
turtle.Screen().bgcolor(colorbg)
square = turtle.Turtle()
ang = 360/4
for i in range(4):
    square.forward(200)
    square.right(ang)
turtle.done()