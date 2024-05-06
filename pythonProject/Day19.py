#more turtle module
from turtle import *
import random
def move_foward():
    forward(20)
def turn_right():
    setheading(heading()-10)

def turn_left():
    setheading(heading() + 10)

def move_backward():
    right(180)
    forward(20)
screen = Screen()

# onkey(move_foward, "w")
# onkey(move_backward, "s")
# onkey(turn_left, "a")
# onkey(turn_right, "d")

screen.setup(500,400)
guess = screen.textinput("Choose one, make a bet" , "Which turtle will win this race?")
colors = ["red","yellow","blue","black","green"]
yPos = [-70,-40,-10,20,50]

def goal():
    goals = Turtle()
    goals.hideturtle()
    goals.penup()
    goals.goto(230,100)
    goals.right(90)
    goals.pendown()
    goals.forward(200)

goal()
all_Turtle = []

for turtle_s in range(0, 5):
    Create_turtle = Turtle("turtle")
    Create_turtle.penup()
    Create_turtle.color(colors[turtle_s])
    Create_turtle.goto(-230, yPos[turtle_s])
    all_Turtle.append(Create_turtle)

race_is_true = True
while race_is_true:
    for turtle in all_Turtle:
        if turtle.xcor() > 230:
            race_is_true = False
            turtle_Color_winning = turtle.pencolor()
            if turtle_Color_winning == guess:
                print(f"You guess is correct. {turtle_Color_winning} are the winner.")
            else:
                print(f"You wrong. The winner is {turtle_Color_winning}")
        rand_speed = random.randint(5,15)
        turtle.forward(rand_speed)




listen()
screen.exitonclick()