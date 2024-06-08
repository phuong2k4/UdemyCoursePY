# with open("ExDay25/DataWeather.csv") as File:
#     read = File.readlines()
#     print(read)
import turtle

# import csv
# with open("ExDay25/DataWeather.csv") as Data:
#     data = csv.reader(Data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
# print(temperatures)

import pandas

# data = pandas.read_csv("ExDay25/DataWeather.csv")
# data_dict = data.to_dict()


# sum1 =0
# for deg in data["temp"].tolist():
#     sum1 += deg
# sum1/=len(data["temp"].tolist())
# print(sum1)

# convert list
# data_temp_list = data["temp"].tolist()
# total = sum(data_temp_list) / len(data_temp_list)
# print(total)

# method csv
# method_mean = data["temp"].mean()
# method_max = data["temp"].max()
# print(method_mean)

# get data of column
# print(data.condition)


# get rows in data by method
# print(data[data.day == "Monday"])

# challenge
# for temp in data["temp"]:
#     if temp == data["temp"].max():
#         print(data[data.temp == temp])

# print(data[data.temp == data.temp.max()])

# monday_data = data[data.day == "Monday"]
# print(((monday_data.temp) * 9/5) + 32)


# data frame from scratch
# new_data = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_n = pandas.DataFrame(new_data)
# data_n.to_csv("ExDay25/new_data.csv")

# 004 challenge:
# data = pandas.read_csv("ExDay25/2018-data-nyc.csv")

# export_file = pandas.DataFrame(furcolor_data)
# grey_count = len(data[data["Primary Fur Color"] == "Grey"])
# red_count = len(data[data["Primary Fur Color"] == "Red"])
# black_count = len(data[data["Primary Fur Color"] == "Black"])
#
# fur_color = {
#     "Fur color": ["Grey", "Red", "Black"],
#     "Count": [
#         grey_count,
#         red_count,
#         black_count
#     ]
# }
# data_export = pandas.DataFrame(fur_color)
# data_export.to_csv("ExDay25/ExportFile.csv")

from turtle import *

screen = Screen()
screen.title("Us State Game")
img = "ExDay25/blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)

def get_mouse_click_coor(x,y):
    print(x, y)

states_correct = []
data_us_states = pandas.read_csv("ExDay25/50_states.csv")
while len(states_correct) < 50:
    answer_state = screen.textinput(title=f"{len(states_correct)}/50 Guess the States" , prompt="Whats the next state's name?")
    if answer_state in data_us_states.state.to_list():
        states_correct.append(answer_state)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        states = data_us_states[data_us_states.state == answer_state]
        tur.goto(int(states.x), int(states.y))
        tur.write(answer_state)
    if answer_state == "exit":
        missing_state = []
        for state in data_us_states.state.to_list():
            if state not in states_correct:
                missing_state.append(state)
        export_missing = pandas.DataFrame(missing_state)
        export_missing.to_csv("ExDay25/Missing_States.csv")
        break
screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()