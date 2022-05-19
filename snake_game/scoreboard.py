from turtle import Turtle
ALIGNMENT = 'CENTER'
FONT = ('Arial',15,'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #read existing high_score from the high_score.txt file
        with open('./high_score.txt') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.penup()
        self.goto(x=0,y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0,y=270)
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER!!!!", align=ALIGNMENT, font=FONT)
        
        
