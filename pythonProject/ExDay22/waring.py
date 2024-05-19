from turtle import *

class Alarm(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 0)
        self.write("You lose, Play again! ", move="center", font=50 )