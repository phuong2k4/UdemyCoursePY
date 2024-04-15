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

# names_string = "phuong,phong,quynh,bao"
# names = names_string.split(", ")
# import random
#
# total = len(names)
# random_in_string = random.randint(0, total - 1)
# pay_guys = names[random_in_string]
#
# print(f"The pay guy today is {pay_guys}")

list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]

map = [list1, list2, list3]

hidding_treasure = input("Where do you want to put a treasure?")

letter = hidding_treasure[0].lower()
text = ["a", "b", "c"]

letter_index = text.index(letter)
number_index = int(hidding_treasure[1])-1
map[number_index][letter_index] = "X"

print(f"{list1} \n {list2} \n {list3}")
