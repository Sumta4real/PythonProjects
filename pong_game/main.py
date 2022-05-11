from turtle import Screen
from pad import Pad
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong Game')
screen.tracer(0)

#Create two Pad objects to represent the right and left paddle
right_pad = Pad((360,0))
left_pad = Pad((-360,0))
ball = Ball()
scoreboard = Scoreboard()

#write the game code

#control instructions for the pads
screen.listen()
screen.onkey(right_pad.move_up,"Up")
screen.onkey(right_pad.move_down,"Down")
screen.onkey(left_pad.move_up,"u")
screen.onkey(left_pad.move_down,"d")

game_on = True
new_time = 0.1

while game_on:
    screen.update()
    time.sleep(new_time)
    ball.move()

    #Detect collision of ball with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
        

    #Detect collision with pad
    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        new_time += 0.01
        

    #Detect Right paddle misses
    if ball.xcor() > 380:
        scoreboard.left_score()
        ball.reset_ball()

    #Detect Left paddle misses
    if ball.xcor() < -380:
        scoreboard.right_score()
        ball.reset_ball()







screen.exitonclick()
