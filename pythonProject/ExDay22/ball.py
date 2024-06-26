from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 0.1
        self.y = 0.1

    def move(self):
        xpos = self.xcor() + self.x
        ypos = self.ycor() - self.y
        self.goto(xpos,ypos)

    def bounce_x(self):
        self.x *= -1
    def bounce_y(self):
        self.y *= -1