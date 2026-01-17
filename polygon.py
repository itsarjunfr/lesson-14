import turtle
turtle.Screen().bgcolor('orange')
polygon = turtle.Turtle()
num = int(input('Number of sides of polygon: '))
length = 70
ang = 360/num
for i in range(num):
    polygon.forward(length)
    polygon.right(ang)
turtle.done()