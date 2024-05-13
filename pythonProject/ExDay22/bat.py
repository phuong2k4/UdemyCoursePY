
from turtle import *

class BatBaseBall():
    def __init__(self):
        self.move = Turtle()
    def myBat(self):
        mBat = Turtle("square")
        mBat.color("white")
        mBat.shapesize(10, 2)
        mBat.penup()
        mBat.goto(600,0)
        pendown()

    def botBat(self):
        botBat = Turtle("square")
        botBat.color("white")
        botBat.shapesize(10, 2)
        botBat.penup()
        botBat.goto(-600,0)
        pendown()

    def up(self):
        newY = self.move.xcor() + 20
        self.move.goto(self.move.xcor(), newY)

    def down(self):
        newY = self.move.xcor() - 20
        self.move.goto(self.move.xcor(), newY)