#more about function
#with argument and parameter
# def person(name, age):
#     print(f"My name is {name} and now im {age}")
#     if age < 18:
#         print("Im a student in My Loc High school. ")
#     else:
#         print("Now imma a colege")
#
# person("Phuong",20)
#
#import math
#from math import ceil
# def solution(height,weight,coverage):
#     total_of_can = (height * weight) / coverage
#     print(ceil(total_of_can))
#
# height_input = int(input("Height: "))
# weight_input = int(input("Weight: "))
# coverage = 5
#
# solution(height_input,weight_input,coverage)

# def primer_checker(number):
#     is_prime = True
#     for index in range(2, number ):
#         if number % index == 0:
#             is_prime = False
#     if is_prime == True:
#         print("Y")
#     else:
#         print("N")
# num_input = int(input("Your number: "))
#
# print(primer_checker(num_input))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Import and print the logo from art.py when the program starts.
from ExtentionD8.art import logo
print(logo)

restart = False

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  for ind in start_text:
    position = alphabet.index(ind)
    new_position = position
    if cipher_direction == "encode":
      new_position += shift_amount
    elif cipher_direction == "decode":
      new_position -= shift_amount
    text_new = alphabet[new_position]
    end_text += text_new
  print(f"Here's the {cipher_direction}d result: {end_text}")

shift %= 26
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

user = input("Wanna do it again? ")
if user == "yes":
  restart = True
elif user == "no":
  restart = False

while restart==True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  break