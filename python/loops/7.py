import random
highest=100
answer=random.randint(1,highest)
guess=int(input(f"Please guess a number between 1 and {highest}: "))
if guess==answer:
    print("you guessed it on first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess=int(input())
    if guess==answer:
        print("well done you guessed it")
    else:
        print(f"Sorry ,The correct answer is {answer}")
    
