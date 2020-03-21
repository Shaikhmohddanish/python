import random
highest=10
guess=int(input(f"please Enter a number between 1 and {highest} "))
answer=random.randint(1,highest)
guesses=1
if guess==answer:
    print("Well done you got it in 1st time")
else:
    while True:
        if guess<answer:
            print("please guess higher")
        else:
            print("please guess lower")
        guess=int(input())
        if guess==answer:
            print(f"Well done you guessed in {guesses} guess ")
            break
        guesses=guesses+1