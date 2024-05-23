from turtle import *


distance = 20
step_by_step = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.move = []
        self.snake_initialization()
        self.head = self.move[0]
    def snake_initialization(self):
        for steps in step_by_step:
            self.add_segment(steps)

    def add_segment(self, steps):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(steps)
        self.move.append(snake)

    def when_hit_food(self):
        self.add_segment(self.move[-1].position())

    def move_Snake(self):
        for steps in range(len(self.move)-1, 0, -1):
            xLocation = self.move[steps - 1].xcor()
            yLocation = self.move[steps - 1].ycor()
            self.move[steps].goto(xLocation, yLocation)
        self.head.forward(distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def respawn(self):
        for part in self.move:
            part.goto(1000,1000)
        self.move.clear()
        self.snake_initialization()
        self.head = self.move[0]

