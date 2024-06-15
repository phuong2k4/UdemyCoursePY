# Error in python

# --- key error --- #
# dictionary = {
#     "key": "value"
# }
# value = dictionary["key_error"]


# --- Index error --- #
# array = [0,1,2,3,4]
# temp = array[5]


# --- type error ---#
# string = "abcd"
# for i in string:
#     i+=1

# Python try catch
# try catch except finally parttern

# Co gang try lam cai nay
# try:
#     file = open("file_txt.txt")
#     data = {"key": "value"}
#     print(data["key"])
# # try khong duoc ma ra error thi except cai nay
# except FileNotFoundError:
#     file = open("file_txt.txt","w")
#     file.write("Somthing in here. ")
# except KeyError as notfound:
#     print(f"Key {notfound} not found.")
# # neu try duoc thi lam cai nay
# else:
#     content = file.read()
#     print(content)
# # else xong roi thi don dep
# finally:
#     raise TypeError("I made this error =>")
#     # file.close()
#     # print("File is close! ")

# raise create alert error in terminal

# challenge
# fruits = eval(input())
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + "pie")
#
# make_pie(4)


# challenge
# example = [{"Like": 2, "comments": 3} , {"Like": 11, "comments": 10}, {"Like": 1, "comments": 5, "Share": 1}, {"Share": 1, "comments": 6}, {"Share": 1, "comments": 2}]
# facebook_post = eval(input())
#
# total_like = 0
#
# for post in facebook_post:
#     try:
#         total_like += post["Like"]
#     except KeyError:
#         pass
#
# print(total_like)


# exception handling
# import pandas
# data = pandas.read_csv("nato_alphabet2.csv")
# # convert csv file to dict in python use dictionary comprehension
# # {keyword:value for namekeyword in data}
# convert_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# def generator():
#     user_word_typing = input("Enter a word: ").upper()
#     try:
#         # list comprehension [keyword for key in object]
#         output = [convert_dict[letter] for letter in user_word_typing]
#     except KeyError:
#         print("Just a name or word. Dont use number or any type different!")
#         generator()
#     else:
#         print(output)
# generator()


# JSON data
# json.dump() # write
# json.load() # read
# json.update() # update
