#Rock Paper Scissor game

import random

option = ["rock", "paper", "scissors"]

user_selected = input("Choose rock, paper, or scissors: ")

computer_selected = random.choice(option)

print("User chose:", user_selected)
print("Computer chose:", computer_selected)

if user_selected == computer_selected:
    print("It's a tie!")
elif user_selected== "rock" and computer_selected == "scissors":
    print("As rock smashes scissors so You win this game")
elif user_selected == "paper" and computer_selected == "rock":
    print("As paper covers rock So You win this game")
elif user_selected == "scissors" and computer_selected == "paper":
    print("As scissors cuts paper so You win this game")
else:
    print("You lost this game")
