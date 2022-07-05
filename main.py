import turtle
import random

#Screen
wn = turtle.Screen()
wn.bgcolor('green')

class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.shapesize(2,2)
        self.up()
        self.color('red')
        self.dx = -0.5
        self.goto(420, random.randint(0,250))

#drawborder
my_pen = turtle.Turtle()
my_pen.penup()
my_pen.setposition(-300,-300)
my_pen.pendown()
my_pen.pensize(4)
for _ in range(4):
    my_pen.forward(600)
    my_pen.left(90)
my_pen.hideturtle()

speed = 1
#create player turtle 
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)

#key listen
def turnleft():
    player.left(15)

def turnright():
    player.right(15)



turtle.listen()
turtle.onkeypress(turnleft,'Left')
turtle.onkeypress(turnright,'Right')
wn.listen()




while True:
    if abs(player.position()[0]) > 300:
        player.setposition(-player.position()[0],player.position()[1])
    if abs(player.position()[1]) > 300:
        player.setposition(player.position()[0],-player.position()[1])
    player.forward(3)

