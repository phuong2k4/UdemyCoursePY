#objects and accessing

#
# from turtle import Turtle, Screen
#
# test = Turtle()
# print(test)
# test.shape("turtle")
# test.color("coral")
# test.backward(250)
# my_Screen = Screen()
#
# print(my_Screen.canvheight)
# my_Screen.exitonclick()

# import turtle
#
# # Tạo một cửa sổ đồ họa
# window = turtle.Screen()
#
# # Tạo một đối tượng rùa
# alex = turtle.Turtle()
#
# # Vẽ hình vuông
# for _ in range(4):
#     alex.forward(100)  # Di chuyển về phía trước 100 bước
#     alex.left(90)      # Rẽ trái 90 độ
#
# # Đóng cửa sổ khi nhấp chuột vào cửa sổ
# window.mainloop()

# graphics in py
# from prettytable import PrettyTable
#
# windows = PrettyTable()
# windows.field_names = ["Name", "Age" , "Gender"]
# windows.add_row(["Phuong", 21, "Male"])
# windows.add_row(["Nam", 21, "Male"])
# windows.add_row(["Cuc", 22, "FeMale"])
#
# windows.align["Name"] = "l"   # Canh trái cho cột "Name"
# windows.align["Age"] = "r"    # Canh phải cho cột "Age"
# windows.align["Gender"] = "c"
#
# print(windows)


# coffee machine use oop or object-oriented-programming

from ExDay16.menu import Menu, MenuItem
from ExDay16.make_coffee import CoffeeMaker
from ExDay16.money_machine import MoneyMachine

money_machine = MoneyMachine()
make_coffee = CoffeeMaker()

menu = Menu()
is_loop = True

while is_loop:
    options = menu.get_items()
    print("Can i help you about menu or something The coffee house?")
    choice = input(f"{options}? Lets take one and enjoy: ")
    if choice == "report":
        make_coffee.report()
        money_machine.report()
    elif choice == "off":
        is_loop = False
    else:
        drink = menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            make_coffee.make_coffee(drink)
