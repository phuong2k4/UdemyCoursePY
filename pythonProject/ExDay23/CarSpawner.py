import random
from turtle import Turtle

COLORS = ["red", "blue", "green", "brown", "yellow", "purple"]
START_DISTANCE = 0.1
MOVE_INCREMENT= 0.3

class carManager():
    def __init__(self):
        self.all_car = []
        self.speed = START_DISTANCE
    def spawn(self):
        spawn_in_per = random.randint(1,1000)
        if spawn_in_per == 10:
            for car_define in COLORS:
                car_define = Turtle()
                car_define.shape("square")
                car_define.penup()
                car_define.shapesize(1,2)
                car_define.color(random.choice(COLORS))
                random_y = random.randint(-240,280)
                car_define.goto(300, random_y)
                self.all_car.append(car_define)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.speed)

    def define_car(self):
        self.speed += MOVE_INCREMENT