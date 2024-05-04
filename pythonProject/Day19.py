#more turtle module
from turtle import *

def move_foward():
    forward(50)
def turn_right():
    right(90)
    forward(50)

def turn_left():
    left(90)
    forward(50)
screen = Screen()

onkey(key="space", fun= move_foward)
onkey(key="Right", fun= turn_right)
onkey(key="Left", fun= turn_left)

listen()
screen.exitonclick()