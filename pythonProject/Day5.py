#sum of array
# element_Num = input().split()
# for index in range(0, len(element_Num)):
#     element_Num[index] = int(element_Num[index])
#
# total = 0
#
# for index in range(0, len(element_Num)):
#     total += element_Num[index]
#
# print(total)

#biggest in array
# element_Num = input().split()
# for index in range(0, len(element_Num)):
#     element_Num[index] = int(element_Num[index])
#
# biggest = 0
# for index in range(0, len(element_Num)):
#     if element_Num[index] > element_Num[biggest]:
#         element_Num[biggest] = element_Num[index]
#
# print(f"The biggest number in array is {element_Num[biggest]}")

# Sum of all even number in array
# target = int(input())
# sum = 0
# for index in range(0,target+1,2):
#     # if(index % 2==0):
#         sum += index
#
# print(sum)

# fizzbuzz

# target = int(input("Lets get a number!\n"))
#
# for index in range(1,target + 1):
#     if index % 3 == 0 and index % 5 == 0:
#         print("FizzBuzz")
#     elif index % 3 == 0:
#         print("Fizz")
#     elif index % 5 == 0:
#         print("Buzz")
#     else:
#         print(index)

# solution issue

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for index in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for index in range(1,nr_symbols+1):
    random_symbols = random.choice(symbols)
    password_list += random_symbols

for index in range(1,nr_numbers+1):
    random_numbers = random.choice(numbers)
    password_list += random_numbers

#print(password_list)

password = ""
for index in password_list:
    password += index

print(password)