#snake solution
from turtle import *
from ExDay20.snake import Snake
import time


main_stream = Screen()
main_stream.bgcolor("black")
main_stream.title("The Snake Game Project")
main_stream.setup(600,600)
main_stream.tracer(0)


snake = Snake()
main_stream.onkey(snake.up, "Up")
main_stream.onkey(snake.down, "Down")
main_stream.onkey(snake.right, "Right")
main_stream.onkey(snake.left, "Left")

main_stream.listen()
game_play = True

while game_play:
    main_stream.update()
    time.sleep(0.1)
    snake.move_Snake()


main_stream.exitonclick()