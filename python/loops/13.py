low=1
high=10
print(f"please guess a number between {low} and {high} : ")
input("Press ENTER to start ")
guesses=1
while low!=high:
    print(f"\t\tGuessing in the range {low} to {high}")
    guess=low +(high-low)//2
    high_low=input(f"My guess is {guess}. Should i guess higher or lower?"
                    "Enter h or l,or c if my guess was correct :").casefold()
    if high_low=="h":
        low=guess+1
    elif high_low=="l":
        high=guess-1
    elif high_low=="c":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("Please enter h, l or c")
    guesses=guesses+1
else:
    print(f"You thought of the number {low}")
    print(f"You got it in {guesses} guesses.")