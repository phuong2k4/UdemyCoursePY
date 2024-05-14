from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()


    def move(self):
        xpos = self.xcor() + 0.1
        ypos = self.ycor() - 0.1
        self.goto(xpos,ypos)