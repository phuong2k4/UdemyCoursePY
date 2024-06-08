from turtle import Turtle

Font = ("JetBrains Mono", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.lever = 1
        self.penup()
        self.hideturtle()
        self.goto(-260,260)


    def notify(self):
        self.clear()
        self.write(f"Lever: {self.lever}", align="left", font=Font)
    def crossroad(self):
        self.lever += 1
        self.notify()

    def lose(self):
        self.clear()
        self.goto(0,0)
        self.write("You Lose. Bastard!", align="center" , font=Font)