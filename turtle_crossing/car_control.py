from calendar import c
from turtle import Turtle
import random


COLORS = ['red','blue','yellow','green','purple','white']
MOVE_DISTANCE = 10

class CarControl():
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_cars(self):
        random_choice = random.randint(0,6)
        if random_choice == 2:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(x=400,y=random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(MOVE_DISTANCE)