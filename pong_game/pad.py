from turtle import Turtle

class Pad(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)

    