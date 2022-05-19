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
        
    def replay(self,to_replay):
        self.to_replay = to_replay
        return self.to_replay.lower() == 'yes'
        
   def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            #Write high_score into the high_score.txt file
            with open('./high_score.txt',mode='w') as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
        
   def goodbye(self,player):
        #self.reset_scoreboard()
        self.clear()
        self.player_name = player
        self.goto(ORIGIN)
        if self.score > self.highscore:
            self.write(f"Thanks {self.player_name.capitalize()} for Playing.\n You Scored {self.score}. \n Current High score is {self.highscore}\n Congrats!!! You are the new highest Scorer", align=ALIGNMENT, font=FONT)
            with open('./high_score.txt',mode='w') as file:
                file.write(f"{self.score}")
        else:
            self.write(f'Thanks {self.player_name.capitalize()} for Playing.\n You Scored {self.score}. \n Current High score is {self.highscore}', align=ALIGNMENT, font=FONT)
    
        
        
