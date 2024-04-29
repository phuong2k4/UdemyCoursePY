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
    "capuchino": {
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
    "coffee": 100
}

profit = 0
def make_coffee_machine(item_coffee):
    """This function check resource have enough or no"""
    for item in item_coffee:
        if item_coffee[item] >= resource[item]:
            print("Sorry there is enough material. ")
            return False
        else:
            return True


def money_machine():
    """This function return total money when user insert cash or coin"""
    total = 0
    print("Just give me my money....")
    total += int(input("How many quarter? Insert: ")) * 0.25
    total += int(input("How many dimes? Insert: ")) * 0.10
    total += int(input("How many nickles? Insert: ")) * 0.5
    total += int(input("How many pennis? Insert: ")) * 0.01
    return total


def transfer_confirm(money_have, menu_cost):
    """Function will return true if money user have is equal or greater than menu cost"""
    if money_have >= menu_cost:
        change = round(money_have - menu_cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += money_have
        return True
    else:
        print("You dont have not enough money. Money Refund")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


cost = 0
loop = True
while loop:
    choice = input("W do you want to drink? Latte, espresso or capuchino: ")
    if choice == "off":
        loop = False
    elif choice == "report":
        print(
            f"Water: {resource["water"]}\n"
            f"Milk: {resource["milk"]}\n"
            f"Coffee: {resource["coffee"]}\n"
            f"Money: {cost}"
            )
    else:
        drink = menu[choice]
        if make_coffee_machine(drink['ingredients']):
            total_user_have = money_machine()
            if transfer_confirm(total_user_have, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

