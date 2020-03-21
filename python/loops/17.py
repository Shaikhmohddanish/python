available_exits=["north","south","east","west"]
choosen_exit=None
while choosen_exit not in available_exits:
    choosen_exit=input("please chooose a direction: ").casefold()
    if choosen_exit.casefold()=="quit":
        print("Game Over")
        break
else:
    print("aren't you glad you got out of there")
