from turtle import Screen, Turtle
from ExDay22.line import *
from ExDay22.bat import *
from ExDay22.ball import Ball

main = Screen()
main.setup(1400,800)
main.bgcolor("black")
main.title("Pong Game")
main.tracer(0)

right_Bat = BatBaseBall((600,0))
left_Bat = BatBaseBall((-600,0))
ball = Ball()

line = Line()


main.listen()
main.onkey(right_Bat.goup, "Up")
main.onkey(right_Bat.godown, "Down")
main.onkey(left_Bat.goup, "w")
main.onkey(left_Bat.godown, "s")


game = True
while game:
    main.update()
    ball.move()
    if ball.ycor() > 800 or ball.ycor() < -800:
        ball.bounce()

main.exitonclick()