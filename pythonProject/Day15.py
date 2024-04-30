#pycharm features
# you can change all name function by retractor
#using retractor -> rename
# def sum(n1, n2):
#     total = n1 + n2
#     return total
#
#
# print(sum(1, 4))
#
#solution coffee machine code


menu = {
    "espresso": {
        "ingredients": {
            "water" : 50,
            "coffee" : 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3
    }
}

resource = {
    "water": 300,
    "milk": 200,
    "coffee" : 100
}
cost = 0

def cash_machine():
    total = 0
    print("How much money do you have right now sir?")
    total += int(input("You got Quarter. Insert: ")) * 0.25
    total += int(input("You got Dime. Insert: ")) * 0.10
    total += int(input("You got Dime. Insert: ")) * 0.5
    total += int(input("You got Dime. Insert: ")) * 0.01
    return total

def make_coffee(choice_drink):
    for item in choice_drink:
        if choice_drink[item] > resource[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def coffee_machine(drink_choice, offer_menu):
    for item in offer_menu:
        resource[item] -= offer_menu[item]
    print(f"Enjoy! {drink_choice}")

def transfer_cash(user_money_have, menu_cost_item):
    if user_money_have >= menu_cost_item:
        change_money_computer = round(user_money_have , 2)
        print(f"Here your cash: ${change_money_computer}")
        global cost
        cost += change_money_computer
        return True
    else:
        print("Not enough money to order this coffee. Refund....")
        return False


game = True

while game:
    print("Can i help you about menu or something The coffee house?")
    choice = input("Latte , espresso or capuchino ? Lets take one and enjoy: ")
    if choice == "report":
        print(f"Water: {resource['water']}")
        print(f"Milk: {resource['milk']}")
        print(f"Coffee: {resource['coffee']}")
        print(f"Cost: {cost}")
    elif choice == "off":
        game = False
    else:
        drink = menu[choice]
        if make_coffee(drink["ingredients"]):
            cash_general = cash_machine()
            if transfer_cash(cash_general,drink["cost"]):
                coffee_machine(choice,drink["ingredients"])