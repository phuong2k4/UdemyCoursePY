#Solution1
# sizeS = 15
# sizeM = 20
# sizeL = 25
# print("Thanks for choosing Python Pizza Deliver")
# size = str(input("What size pizza do you want?"))
# add_pepperoni = str(input("Do you want pepperoni? Yes or No?"))
# add_extra_cheese = str(input("Wanna extra cheese? Brother?"))
# if add_pepperoni == "Y":
#     if(size == "S"):
#         sizeS +=2
#     elif(size == "M"):
#         sizeM +=3
#     elif(size == "L"):
#         sizeL +=3
# if add_extra_cheese == "Y":
#     sizeS += 1
#     sizeM += 1
#     sizeL += 1
# if size == "S":
#     print("The final bill is: " + str(sizeS))
# if size == "M":
#     print("The final bill is: " + str(sizeM))
# if size == "L":
#     print("The final bill is: " + str(sizeL))


#solution2
# name1 = input("My name: \n")
# name2 = input("Her name: \n")
#
# combined_name = name1 + name2
# convert_lower_character = combined_name.lower()
#
# t = convert_lower_character.count("t")
# r = convert_lower_character.count("r")
# u = convert_lower_character.count("u")
# e = convert_lower_character.count("e")
#
# total_first_name = t + r + u + e
#
# l = convert_lower_character.count("l")
# o = convert_lower_character.count("o")
# v = convert_lower_character.count("v")
# e = convert_lower_character.count("e")
#
# total_last_name = l + o + v + e
#
# totalOfAll = total_first_name + total_last_name
#
# if totalOfAll > 10 | totalOfAll < 90:
#     print("Your score is " + str(totalOfAll) + "You go together like coke and mentos")
# elif totalOfAll>40 & totalOfAll<50:
#     print("Your score is " + str(totalOfAll) + " You are alright together")
# else:
#     print("Your score is " + str(totalOfAll))

#last solution
print("Welcome to treasure Island. Your mission is to find the treasure.")
cross_road = str(input("You're at a cross road. Where are you want to go? Left or Right?\n"))

if cross_road == "left":
    island = str(input("You come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for a boad. Type 'swim' to swim across\n"))
    if island == "wait":
        house = str(input("There is 3 doors. Red blue and yellow! Choose one of them!\n"))
        if house == "yellow":
            print("Smart choice! You win this game")
        else:
            print("Loser")
    else:
        print("Game Over")
else:
    print("Dumb")

