from turtle import Turtle


start_position = (0,-280)
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


    def if_turtle_crossroad(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def win_round(self):
        self.goto(start_position)

