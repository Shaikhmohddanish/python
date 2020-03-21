list="1.Learn Python.\n2.Learn Java.\n3.Go to Swimming.\n4.Goto Bed\n5.Dinner\n0.Exit"
print(list)
while True:
    user=int(input("Please select Option: "))
    if user==1:
        print("To padh na python")
    elif user==2:
        print("To padh na Java")
    elif user==3:
        print("To tair na jaake")
    elif user==4:
        print("To so na")
    elif user==5:
        print("To khaaa na")
    elif user==0:
        break
    else:
        print("valid option select kar")
