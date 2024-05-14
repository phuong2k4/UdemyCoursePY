
from turtle import *

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,-800)
        self.pendown()
        self.goto(0,800)
        self.penup()


