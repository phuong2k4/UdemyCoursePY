from turtle import *
from ExDay22.line import *
from ExDay22.bat import *

main = Screen()
main.setup(1400,800)
main.bgcolor("black")

line = Line()
bat = BatBaseBall()



game = True


main.listen()
main.onkey(bat.myBat().up, "Up")
main.onkey(bat.down, "Down")
main.exitonclick()