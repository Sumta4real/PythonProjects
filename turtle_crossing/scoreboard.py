from turtle import Turtle

ALIGNMENT = 'CENTER'
FONT = ('Arial',15,'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0,y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 5
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER!!!!", align=ALIGNMENT, font=FONT)
