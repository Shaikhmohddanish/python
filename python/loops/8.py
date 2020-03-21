f=lambda a:a**2
while True:
    a=int(input("Please enter number you want to square it : "))
    print(f(a))
    b=input("You want to square another number is yes press y and for no press n : ")
    if b.casefold()=="n":
        break
    elif b.casefold()=="y":
        pass
    else:
        print("Please enter valid key : ")