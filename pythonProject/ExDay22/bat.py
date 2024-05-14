
from turtle import *

class BatBaseBall(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(10,2)
        self.penup()
        self.goto(position)


    def goup(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def godown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)