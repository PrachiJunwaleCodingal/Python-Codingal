#Number Game

import random 
playing = True 
number = str(random.randint(10,20)) 

print("Lets guess number between 10 to 20")
print("The game ends when you guess correct number")

while playing:
    guess = input("Enter guess number:")
    if number == guess:
        print("Correct guess")
        print("The number was",number)
        break

    else:
        print("Wrong Guess. Try Again \n")