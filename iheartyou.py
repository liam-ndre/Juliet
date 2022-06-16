import turtle
from turtle import *

wn = Screen()
wn.bgcolor('black')

t = turtle.Turtle()
t.pencolor('white')
turtle.speed(0)
def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht

def write(message, pos):
    x,y = pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style = ('Stencil Std', 18, 'italic')
    t.write(message, font=style)
    t.hideturtle()

write('I', (-60, 95))
write('L', (-38, 95))
write('O', (-25, 95))
write('V', (-9, 95))
write('E', (6, 95))
write('Y', (30, 95))
write('O', (44, 95))
write('U', (59, 95))
write('3', (-30, 60))
write('0', (-15, 60))
write('0', (0, 60))
write('0', (15, 60))


write("You're one in a million", (-100, -150))

wn.mainloop()
