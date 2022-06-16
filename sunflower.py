import turtle
ws = turtle.Screen()
ws.bgcolor("black")
#Define Screen Size
ws.setup(width=1280, height=720)
alex = turtle.Turtle()
alex.speed(0)
alex.pensize(.1)
alex.shape("turtle")

#Petal only
def petal():
    alex.color("black", "yellow")
    alex.begin_fill()
    alex.right(20)
    alex.forward(100)
    alex.left(40)
    alex.forward(100)
    alex.left(140)
    alex.forward(100)
    alex.left(40)
    alex.forward(100)

#seedsInner
for i in range(250):

    if i <200:
        alex.penup()
        alex.forward(i)
        alex.pendown()
        alex.color("black","orange")
        alex.begin_fill()
        alex.stamp()
        alex.left(137.58)
        alex.end_fill()
        i = i + 20
        print("Seed count"+ str(i))
    else:
        alex.penup()
        alex.setposition(0,0)
        alex.forward((i + 30)/2.5)
        alex.pendown()
        alex.color("black", "yellow")
        alex.begin_fill()
        petal()
        alex.left(22/7)
        alex.end_fill()
        i = i + 10
        print("Petal count"+ str(i))

ws.exitonclick()
