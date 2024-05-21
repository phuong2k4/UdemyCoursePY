from turtle import Turtle

class Control(Turtle):
    def __init__(self):
        """Define turtle"""
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(0, -280)
        self.x = self.xcor()
    def moveForward(self):
        """Control turtle and move 10 unit"""
        newy = self.ycor() + 10
        self.goto(self.x, newy)