# Author giri110890
import random

start_score = 0
scores = open('rating.txt', 'r')
scores_record = {}
for line in scores:
    name, score = line.split()
    scores_record[name] = int(score)
user = input("Enter your name:")
print("Hello, {}".format(user))
if user in scores_record:
    start_score = scores_record[user]
game_options = input()
print("Okay, let's start")
while True:
    user_choice = input()
    if game_options == "":
        computer_choice = random.choice(["rock", "paper", "scissors"])
    else:
        computer_choice = random.choice(game_options.split(","))
    game_combination = {"rock": ["fire", "scissors", "snake", "human", "tree", "wolf", "sponge"],
                        "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"],
                        "scissors": ["snake", "human", "tree", "wolf", "sponge", "paper", "air"],
                        "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"],
                        "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
                        "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
                        "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lightning"],
                        "sponge": ["paper", "air", "water", "dragon", "devil", "lightning", "gun"],
                        "paper": ["air", "water", "dragon", "devil", "lightning", "gun", "rock"],
                        "air": ["water", "dragon", "devil", "lightning", "gun", "rock", "fire"],
                        "water": ["dragon", "devil", "lightning", "gun", "rock", "fire", "scissors"],
                        "dragon": ["devil", "lightning", "gun", "rock", "fire", "scissors", "snake"],
                        "devil": ["lightning", "gun", "rock", "fire", "scissors", "snake", "human"],
                        "lightning": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
                        "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"],
                        }
    if user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == "!rating":
        print(start_score)
    elif user_choice not in game_combination:
        print("Invalid input")
    else:
        if user_choice == computer_choice:
            print("There is a draw ({})".format(user_choice))
            start_score += 50
        else:
            if computer_choice in game_combination[user_choice]:
                print("Well done. Computer chose {} and failed".format(computer_choice))
                start_score += 100
            else:
                print("Sorry, but computer chose {}".format(computer_choice))
scores.close()
