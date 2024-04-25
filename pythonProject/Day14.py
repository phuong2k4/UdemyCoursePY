import random
from ExDay14 import art
from ExDay14 import Data
print(art.logo)

print("Who you think they have more followers?")

compareA = random.choice(Data.data)
against = random.choice(Data.data)

print(compareA)
print(art.vs)
print(against)
user = input("Type A or B: ")
point = 0

if user == "A" and compareA["follower_count"] > against["follower_count"]:
    point += 1
elif user == "B" and compareA["follower_count"] < against["follower_count"]:
    point += 1
else:
    print("Lose")
