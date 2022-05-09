from turtle import Turtle

#constant are named with all capss in Python
STARTING_POSITIONS = [(-20,0),(0,0),(20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Build the snake

class Snake():
    """
    Build three square turtles side by side and combine all in a list to represent a snake
    """

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
          for position in STARTING_POSITIONS:
              self.add_part(position)
    
    def add_part(self,position):
        new_part = Turtle(shape='square')
        new_part.color('white')
        new_part.penup()
        new_part.goto(position)
        self.parts.append(new_part)

    def extend(self):
        #add a new part to the snake 
        self.add_part(self.parts[-1].position())

    def move(self):#Move the snake
        for part_num in range(len(self.parts) -1,0,-1):
            new_x = self.parts[part_num -1].xcor()
            new_y = self.parts[part_num -1].ycor()
            self.parts[part_num].goto(new_x,new_y)
    
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        

   
    
        
