available_exists=['east','west','north','south']
chooosen_exit=''
while chooosen_exit not in available_exists:
    chooosen_exit=input("please enter a direction: ")
    if chooosen_exit=='quit':
        print("Game Over")
        break
print("Aren't you glad you got of there")