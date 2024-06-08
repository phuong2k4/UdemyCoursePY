
#global scope
# variable = 5
# def acess():
#     print(variable)
# acess()
#
# #local scope
# def entry():
#     element = 5
#     print(element)
# #print(element) // element is not defined
#
# #Modifying global scope
#
# elemt = 123
# def modify():
#     """Same location in memory"""
#         # global elemt
#     print(f"{elemt} in local scope. ")
#     #or
#     return elemt + 1
# modify()
# print(f"{elemt} in global scope. ")

#solution: guess a number

import random
from ExDay12 import art

print(art.logo)

easy_level = 10
hard_level = 5
answer = random.randint(1,100)
def check_answer(user_guess, answer):
    if user_guess > answer:
        print("Too high. ")

    elif user_guess < answer:
        print("Too low. ")

    elif user_guess == answer:
        print(f"You win. {user_guess} is correct number. ")

def level():
    choose_level = input("We have choice. Easy or hard?. Take one of them. ")
    if choose_level == "easy":
        return easy_level
    if choose_level == "hard":
        return hard_level

print("Take a number. Between 1 and 100. Lets take that!")
def game():
    level_choose = level()
    user_guess = 0

    while user_guess != answer:
        print(f"You have {level_choose}" )
        user_guess = int(input("Make a guess: "))
        check_answer(user_guess,answer)
        if user_guess != answer:
            level_choose -= 1
        if level_choose == 0:
            print("You lose. ")
            return

game()


