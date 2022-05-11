from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_point = 0
        self.right_point = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0,260)
        self.write(f'Score:{self.left_point},{self.right_point}',align='center',font=('Arial',15,'normal'))
    
    def left_score(self):
        self.left_point += 1
        self.clear()
        self.update_scoreboard()
    
    def right_score(self):
        self.right_point +=1
        self.clear()
        self.update_scoreboard()

