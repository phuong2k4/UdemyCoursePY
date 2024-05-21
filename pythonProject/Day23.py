import time
from turtle import *
from ExDay23.Control import *
from ExDay23.CarSpawner import *
from ExDay23.Scoreboard import *

times_when_win = 0.1

screen = Screen()
screen.setup(600,600)
screen.tracer(0)

#define turtle and control
control_Turtle = Control()
score = ScoreBoard()
car = carManager()

screen.listen()
screen.onkey(control_Turtle.moveForward, "Up")

game = True
while game:
    screen.update()
    car.spawn()
    car.move_car()
    score.notify()

    #if turtle touch to the car
    for cars in car.all_car:
        if cars.distance(control_Turtle) < 20:
            game = False
            screen.clear()
            score.lose()
    if control_Turtle.if_turtle_crossroad():
        control_Turtle.win_round()
        car.define_car()
        score.crossroad()

screen.exitonclick()