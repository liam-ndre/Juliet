import turtle
ws = turtle.Screen()
ws.bgcolor("black")
#Define Screen Size
ws.setup(width=1280, height=720)
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pensize(.1)
turtle.shape("turtle")

#Petal only
def petal():
    turtle.color("black", "yellow")
    turtle.begin_fill()
    turtle.right(20)
    turtle.forward(100)
    turtle.left(40)
    turtle.forward(100)
    turtle.left(140)
    turtle.forward(100)
    turtle.left(40)
    turtle.forward(100)

#seedsInner
for i in range(250):

    if i <200:
        turtle.penup()
        turtle.forward(i)
        turtle.pendown()
        turtle.color("black","orange")
        turtle.begin_fill()
        turtle.stamp()
        turtle.left(137.58)
        turtle.end_fill()
        i = i + 20
    else:
        turtle.penup()
        turtle.setposition(0,0)
        turtle.forward((i + 30)/2.5)
        turtle.pendown()
        turtle.color("black", "yellow")
        turtle.begin_fill()
        petal()
        turtle.left(22/7)
        turtle.end_fill()
        i = i + 10

ws.exitonclick()
turtle.hideturtle()
