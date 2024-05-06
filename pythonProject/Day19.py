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

screen.setup(500,400)
screen.textinput("Choose one, make a bet" , "Which turtle will win this race?")

colors = ["red","yellow","blue","black","green"]

for turtle_,i in range(0, 5):
    display = Turtle("turtle")
    display.penup()
    y = 30 * i
    display.goto(-230, y)

listen()
screen.exitonclick()