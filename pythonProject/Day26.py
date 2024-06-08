# List comrehension

# Normal loop list
# numbers = [1, 2, 3]
# news_list = []
# for n in numbers:
#     add_one = n + 1
#     news_list.append(add_one)
# print(news_list)

# using list comprehension (challenge 001)
# news_list = [item + 1 for item in numbers]
# print(news_list)

# Extension List comprehension (challenge 002)
# names = ["Alex", "Beth", "Caroline" , "Dave", "Elanor", "Freddie"]
# uppercase_Len_Names = [name.upper() for name in names if len(name) > 5]

# challenge 003
# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

# challenge 006
# with open("ExDay26/file1.txt") as data_file1:
#     convert_list = data_file1.readlines()
# with open("ExDay26/file2.txt") as data_file2:
#     convert_list2 = data_file2.readlines()
# result = [int(nums) for nums in convert_list if nums in convert_list2]
# print(result)

# Dictionary comprehension
# new_dict = {new_key:new_value for item in list}

# challenge 008
# sentence = input()
# string_split = {character:len(character) for character in sentence.split(" ") }
# print(string_split)

# challenge 009
# {"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thusday": 11, "Friday": 12, "Saturday": 14, "Sunday": 16}
# weather_c = eval(input())
# weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# challenge 010
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(f"{key} and {value}")

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
# for (index, rows) in student_data_frame.iterrows():
#     print(rows.student)

# solution End Day 26

import pandas

data = pandas.read_csv("ExDay26/nato_alphabet.csv")

export_data = {row.letter:row.code for (index, row) in data.iterrows()}

user_name = input("Enter your name: ").upper()

solution = {character:export_data[character] for character in user_name}

print(solution)
# end