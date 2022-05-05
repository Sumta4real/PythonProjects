import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.shape('turtle')

colours = ['blue','red','yellow','purple','gold','green','black']

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for i in range(3,11):
    my_turtle.color(random.choice(colours))
    draw_shape(i)

screen = t.Screen()
screen.exitonclick()