import random
playing=True
number=str(random.randint(10,20))
print("lets guess the number bet 10-20. game will end if you have guess correct no.")

while playing:
    guess=input("enter any no. between 10 to 20 :")
    if number==guess:
        print("correct guess")
        break

    else:
        print("wrong number")