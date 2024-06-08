#snake solution
from turtle import *
from ExDay20.snake import Snake
from ExDay20.Food import Eat_Food
from ExDay20.scoreboard import ScoreB
import time


main_stream = Screen()
main_stream.bgcolor("black")
main_stream.title("The Snake Game Project")
main_stream.setup(600,600)
main_stream.tracer(0)


snake = Snake()
food = Eat_Food()
score = ScoreB()

# key control
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

    #Eat_food (When the snake touch to this point)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.when_hit_food()
        score.add_sc()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.high_score()
        snake.respawn()

    for body_parts in snake.move[1:]:
        if snake.head.distance(body_parts) < 1:
            score.high_score()
            snake.respawn()


main_stream.exitonclick()