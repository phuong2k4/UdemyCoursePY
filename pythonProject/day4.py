#random



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

names = names_string.split(", ")
import random

total = len(names)
random_in_string = random.randint(0, names - 1)
pay_guys = names[random_in_string]

print(f"The pay guy today is {pay_guys}")

