
#turtle graphic

from turtle import *
import random
screen = Screen()

#square
while True:
    forward(100)
    left(90)
    if abs(pos()) < 1:
        break

#dash line
for _ in range(0, 11):
    forward(10)
    penup()
    forward(10)
    pendown()

colors = ["white", "teal", "blue", "burlywood"]
def shape(numsides):
    for _ in range(0, numsides):
        angel = 360 / numsides
        forward(100)
        right(angel)

for num_side in range(3, 11):
    color(random.choice(colors))
    shape(num_side)

def num_of_spirograph(num):
    for _ in range(0, int(360 / num)):
        color(random_color())
        circle(90)
        setheading(heading()+num)

num_of_spirograph(10)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


#solution make
penup()
setheading(205)
forward(350)
setheading(0)
speed("fastest")
for _ in range(0, 11):
    for _ in range(0, 11):
        pencolor(random_color())
        dot(30)
        penup()
        forward(50)
        pendown()
        dot(30)
        penup()
    penup()
    backward(550)
    left(90)
    forward(50)
    right(90)
    pendown()

#solution tutorial


hideturtle()
penup()
setheading(220)
forward(300)
setheading(0)
num_of_dot = 100
for dot_count in range(1,num_of_dot+1):
    dot(20,random_color())
    forward(50)
    if dot_count % 10 == 0:
        setheading(90)
        forward(50)
        setheading(180)
        forward(500)
        setheading(0)

screen.exitonclick()