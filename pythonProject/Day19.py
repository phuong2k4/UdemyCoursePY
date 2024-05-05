#more turtle module
from turtle import *

def move_foward():
    forward(20)
def turn_right():
    setheading(heading()-10)

def turn_left():
    setheading(heading() + 10)

def move_backward():
    right(180)
    forward(20)
screen = Screen()

# onkey(move_foward, "w")
# onkey(move_backward, "s")
# onkey(turn_left, "a")
# onkey(turn_right, "d")

Jones = Turtle()
Ethan = Turtle()
David = Turtle()
Travis = Turtle()

Jones.color("red")
Ethan.color("blue")
David.color("violet")
Travis.color("brown")

Jones.setheading(220)
Jones.forward(250)

David.setheading(200)
David.forward(250)

Travis.setheading(180)
Travis.forward(250)

Ethan.setheading(160)
Ethan.forward(250)




listen()
screen.exitonclick()