from turtle import Screen, Turtle
from ExDay22.line import *
from ExDay22.bat import *


main = Screen()
main.setup(1400,800)
main.bgcolor("black")
main.title("Pong Game")
main.tracer(0)

right_Bat = BatBaseBall((600,0))
left_Bat = BatBaseBall((-600,0))

line = Line()
line.dash()


main.listen()
main.onkey(right_Bat.goup, "Up")
main.onkey(right_Bat.godown, "Down")
main.onkey(left_Bat.goup, "w")
main.onkey(left_Bat.godown, "s")

game = True
while game:
    main.update()



main.exitonclick()