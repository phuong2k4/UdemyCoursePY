from turtle import *

class ScoreB(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lose()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center")
    def add_sc(self):
        self.score += 1
        self.clear()
        self.update_score()
    def lose(self):
        self.goto(-100,0)
        self.write("You Lose! Play again. " , "center", font=24)