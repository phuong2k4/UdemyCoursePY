
from turtle import *

class BatBaseBall(Turtle):
    def __init__(self,position):
        super().__init__()
        bat = Turtle("square")
        bat.color("white")
        bat.shapesize(10,2)
        bat.penup()
        bat.goto(position)


    def goup(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def godown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)