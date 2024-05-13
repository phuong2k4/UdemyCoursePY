
from turtle import *

class Line():
    def __init__(self):
        self.dash()


    def dash(self):
        Turtle()
        hideturtle()
        penup()
        color("white")
        goto(0,-800)
        pendown()
        goto(0,800)
