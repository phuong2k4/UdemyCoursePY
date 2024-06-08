#function with output

# def add_parameter(param1, param2):
#     param1.title()
#     param2.title()
#     return f"{param1} {param2}"
#
# f_name = input("Whats u first name? ")
# l_name = input("Whats u last name? ")
#
# print(add_parameter(f_name, l_name))


# year = int(input("Year: "))
# month = int(input("Month: "))
#
# def is_leap(year):
#     """
#     Return leap year or not a leap year
#     (You can just mod 4, result still corectly)
#     """
#     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return False
#
# def days_in_month(year,month):
#     """This function will return a month in leap or not a leap year"""
#     month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
#
# print(days_in_month(year, month))


#solution Caculator:

from ExDay10 import art
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def muti(num1, num2):
    return num1 * num2
def dev(num1, num2):
    return num1 / num2

# if operation == "+":
#     print(f"{num1} {operation} {num2} = {add(num1,num2)}")
# elif operation == "-":
#     print(f"{num1} {operation} {num2} = {sub(num1,num2)}")
# elif operation == "*":
#     print(f"{num1} {operation} {num2} = {muti(num1, num2)}")
# elif operation == "/":
#     print(f"{num1} {operation} {num2} = {dev(num1, num2)}")

operator_symbol = {
    "+": add,
    "-": sub,
    "*": muti,
    "/": dev
}

def calculator():
    print(art.logo)
    num1 = int(input("Whats the first number? "))
    for symbol in operator_symbol:
        print(symbol)
    condition = False

    while not condition:
        num2 = int(input("How about the next number? "))
        operation = input("Pick an operation: ")
        my_operation = operator_symbol[operation]
        answer = my_operation(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        continue_user = input("y to continue calculating. n to start a new calculation. ")
        if continue_user == "y":
            num1 = answer
            condition = False
        elif continue_user == "n":
            condition = True
            calculator()

calculator()


