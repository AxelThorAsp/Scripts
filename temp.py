import time
import turtle
import random
# set screen
sc = turtle.Screen()
sc.setup(800, 800)
sc.tracer(0) 

t = turtle.Turtle()
t.shape('circle')
t.turtlesize(10)
t.penup()
t.goto(-100,-100)


  
# global colors
col = ['red', 'yellow', 'green', 'blue',
       'white', 'black', 'orange', 'pink']
  
# method to call on timer
def fxn(col):
    sc.update()
    ind = random.randint(0, 7)
  
    # set background color of the
    # turtle screen randomly
    t.color(col[ind])
    t.forward(100)
    t.left(35)
    sc.bgcolor(col[random.randint(0,7)])
  
  
 
# loop for timer
sc.ontimer(fxn(col), 1000)
sc.update()
time.sleep(2)