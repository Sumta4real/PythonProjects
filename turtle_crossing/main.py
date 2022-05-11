from turtle import Screen
from player import Player
from car_control import CarControl
import random
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up,'Up')
screen.onkey(player.move_left,'Left')
screen.onkey(player.move_right,'Right')

car = CarControl()
score = Scoreboard()

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_cars()
    car.move_cars()

    #Detect collision of player with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_on = False 
            score.game_over()

    #Detect successful crossing
    if player.reached_finish_line():
        score.increase_score()
        player.back_to_start()
        player.player_speed()



screen.exitonclick()
