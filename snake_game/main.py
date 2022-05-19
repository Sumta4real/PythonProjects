from ast import Pass
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
"""
Build Snake game in seven steps

1. Setup the screen
2. Build the snake
3. Move the snake
4. Control the snake using keyboard controls
5. Detect collision with food
6. Create a scoreboard
7. Detect collision with wall
8. Detect collision with tail
"""
#Set up th screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #stop animation, don't show what's happening on the screen

snake = Snake()
food = Food()
scoreboard = Scoreboard()


game_is_on = True
player_name = screen.textinput(title='Tell your name',prompt='What would you like to be called')
while game_is_on:
    
    screen.listen()
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')

    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    #Detect collision with the tail
    #if head collide with any segment in the tail, trigger game_over
    #for parts in snake.parts[1:]:
        #if snake.head.distance(parts) < 10:
        #    game_is_on = False
        #    scoreboard.game_over()
        
       

    

screen.exitonclick()
