import random
from ExDay14 import art
from ExDay14 import Data
print(art.logo)

print("Who you think they have more followers?")
def game_play():
    compareA = random.choice(Data.data)
    against = random.choice(Data.data)
    end_game = False
    point = 0
    while not end_game:
        print(f"{compareA["name"]} , {compareA["description"]} from {compareA["country"]}")
        print(art.vs)
        print(f"{against["name"]} , {against["description"]} from {against["country"]}")
        user = input("Type A or B: ")

        if user == "A" and compareA["follower_count"] > against["follower_count"]:
            print("You're right. ")
            against = random.choice(Data.data)
            point+=1
            print(f"Current score: {point}")
        elif user == "B" and compareA["follower_count"] < against["follower_count"]:
            print("You're right. ")
            compareA = against
            against = random.choice(Data.data)
            point += 1
            print(f"Current score: {point}")
        elif compareA == against:
            against = random.choice(Data.data)
        else:
            print("Lose")
            end_game = True
    print(f"your final point: {point}")

game_play()