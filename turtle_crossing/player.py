from turtle import Turtle

START = (0,-280)
MOVEMENT = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.back_to_start()
        self.setheading(90)
        self.speed = 10

    def move_up(self):
        y_val = self.ycor() + MOVEMENT 
        self.goto(self.xcor(),y_val)

    def move_left(self):
        x_val = self.xcor() - MOVEMENT 
        self.goto(x_val,self.ycor())

    def move_right(self):
        x_val = self.xcor() + MOVEMENT 
        self.goto(x_val,self.ycor())
    
    def reached_finish_line(self):
        return self.ycor() > FINISH_LINE

    def back_to_start(self):
        self.goto(START)

    def level_up(self):
        self.speed += MOVEMENT