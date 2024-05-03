
#turtle graphic

from turtle import *
import random
screen = Screen()

#square
# while True:
#     forward(100)
#     left(90)
#     if abs(pos()) < 1:
#         break

#dash line
# for _ in range(0, 11):
#     forward(10)
#     penup()
#     forward(10)
#     pendown()

colors = ["white", "teal", "blue", "burlywood"]
def shape(numsides):
    for _ in range(0, numsides):
        angel = 360 / numsides
        forward(100)
        right(angel)

for num_side in range(3, 11):
    color(random.choice(colors))
    shape(num_side)
screen.exitonclick()