import time
from turtle import *
from ExDay23.Control import *
from ExDay23.CarSpawner import *


screen = Screen()
screen.setup(600,600)
screen.tracer(0)

#define turtle and control
control_Turtle = Control()

car = carManager()

screen.listen()
screen.onkey(control_Turtle.moveForward, "Up")


game = True
while game:

    screen.update()

    car.spawn()
    car.move_car()

screen.exitonclick()