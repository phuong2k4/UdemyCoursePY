import random
from replit import clear
from ExDay11 import art

def deal_card():
    cards = [11, 2, 3,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10]
    rand_card = random.choice(cards)
    return rand_card

def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if sum(card) > 21 and 11 in card:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "A good game!"
    elif computer_score == 0:
        return "Dude bro u have a blackjack! u win"
    elif user_score == 0:
        return "I win, lets goooo"
    elif user_score > 21:
        return "Damnn things! u win"
    elif computer_score > 21:
        return "Have a lot. i dont need it =>"
    elif user_score > computer_score:
        return "Im so lucky. Win this game!"
    elif user_score < computer_score:
        return "You deserved it"

def play_game():
    print(art.logo)

    user_card = []
    computer_card = []
    game_play = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_play:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"This your card: {user_card} and total {user_score}")
        print(f"Computer card : {computer_card} and total {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score >21 or computer_score > 21:
            game_play = True
        else:
            continue_user = input("Type 'y' to get another card, 'n' to pass: ")
            if continue_user == "y":
                user_card.append(deal_card())
            else:
                game_play = True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Wanna play blackjack? Type 'y' or 'n'. ") == "y":
    clear()
    play_game()