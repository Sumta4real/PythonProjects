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
        
     def welcome(self,player):
        self.player_name = player
        self.goto(POSITION)
        self.write(f'Welcome {self.player_name.capitalize()} to the Snake Game', align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0,y=270)
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER!!!!", align=ALIGNMENT, font=FONT)
        
   def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            #Write high_score into the high_score.txt file
            with open('./high_score.txt',mode='w') as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
    
        
        
