from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.x_pos = 10
        self.y_pos = 10
        self.pace = 0.1

    def move(self):
        x_new = self.xcor() + self.x_pos
        y_new = self.ycor() + self.y_pos
        self.goto(x_new,y_new)

    def y_bounce(self):
        self.y_pos *= -1
    
    def x_bounce(self):
        self.pace *= 0.9
        self.x_pos *= -1


    def reset_ball(self):
        self.goto(0,0)
        self.x_bounce()