#from os import RWF_SYNC
import turtle as t
import random

rwalk = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]
rwalk.pensize(15)
rwalk.speed(10)

for _ in range(200):
    rwalk.color(random_color())
    rwalk.forward(30)
    rwalk.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()