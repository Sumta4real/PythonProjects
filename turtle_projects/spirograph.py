import turtle as t
import random

spirograph = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

spirograph.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spirograph.color(random_color())
        spirograph.circle(100)
        current_header = spirograph.heading()
        spirograph.setheading(current_header + 10)

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()