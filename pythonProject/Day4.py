#random
# import random

#solution1:
# user = random.randrange(1,3)
# if user == 1:
#     print("Heads")
# elif user == 2:
#     print("Taile")

#list
# human = ["Phong", "Nam", "Thanh"]
# for ind in human:
#     print(ind)

# names_string = "phuong,phong,quynh,bao"
# names = names_string.split(", ")
# import random
#
# total = len(names)
# random_in_string = random.randint(0, total - 1)
# pay_guys = names[random_in_string]
#
# print(f"The pay guy today is {pay_guys}")


#treasure
# list1 = [" ", " ", " "]
# list2 = [" ", " ", " "]
# list3 = [" ", " ", " "]
#
# map = [list1, list2, list3]
#
# hidding_treasure = input("Where do you want to put a treasure?")
#
# letter = hidding_treasure[0].lower()
# text = ["a", "b", "c"]
#
# letter_index = text.index(letter)
# number_index = int(hidding_treasure[1])-1
# map[number_index][letter_index] = "X"
#
# print(f"{list1} \n {list2} \n {list3}")

#final solution

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
three_option = [rock, paper, scissors]

user = int(input("What do you choose? Rock as 0, paper as 1 or scissors as 2?. Take one of them"))

import random

option = len(three_option)
option_convert_interger = random.randint(0,option-1)
pc_choice = three_option[option_convert_interger]

print(three_option[user])
print(pc_choice)

if user == 0 and option_convert_interger==2:
    print("I win this game")
elif option_convert_interger > user:
    print("U lose =>")
else:
    print("we same")
