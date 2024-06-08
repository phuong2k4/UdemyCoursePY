import time
from turtle import Screen, Turtle
# from ExDay22.line import *
from ExDay22.bat import *
from ExDay22.ball import Ball
from ExDay22.waring import Alarm

main = Screen()
main.setup(1400,800)
main.bgcolor("black")
main.title("Pong Game")
main.tracer(0)

right_Bat = BatBaseBall((650,0))
left_Bat = BatBaseBall((-650,0))


ball = Ball()
# line = Line()


main.listen()
main.onkey(right_Bat.goup, "Up")
main.onkey(right_Bat.godown, "Down")
main.onkey(left_Bat.goup, "w")
main.onkey(left_Bat.godown, "s")


game = True
while game:
    main.update()
    ball.move()
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    if ball.xcor() > 700 or ball.xcor() < -700:
        alarm = Alarm()
        game = False
    if ball.distance(right_Bat) < 45 and ball.xcor() > 350:
        ball.bounce_x()
    if ball.distance(left_Bat) < 45 and ball.xcor() < -350:
        ball.bounce_x()
main.exitonclick()