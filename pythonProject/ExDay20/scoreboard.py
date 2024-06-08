from turtle import *

class ScoreB(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.finalscore = 0
        self.lose()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} // High score: {self.finalscore}", align="center")

    def add_sc(self):
        self.score += 1
        self.clear()
        self.update_score()

    def lose(self):
        self.goto(-100,0)
        self.write("You Lose! Play again. " , "center", font=24)

    def high_score(self):
        if self.score > self.finalscore:
            self.finalscore = self.score
            with open("ExDay24/text.txt",  mode = 'w') as file:
                file.write(f"{self.finalscore}")
            with open("ExDay24/text.txt") as file:
                self.finalscore = int(file.read())
        self.score = 0
        self.update_score()
